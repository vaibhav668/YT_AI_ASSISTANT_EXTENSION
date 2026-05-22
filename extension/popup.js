const askBtn = document.getElementById("askBtn");

const questionInput = document.getElementById("questionInput");

const chatContainer = document.getElementById("chatContainer");



function addMessage(text, className) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    messageDiv.classList.add(className);

    messageDiv.innerText = text;

    chatContainer.appendChild(messageDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    return messageDiv;
}



askBtn.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question) return;


    addMessage(question, "user-message");

    questionInput.value = "";


    const loadingMessage =
        addMessage("Thinking...", "ai-message");


    try {

        // Get current active tab
        const tabs = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });


        const currentTab = tabs[0];

        const videoUrl = currentTab.url;


        // Check if current tab is YouTube
        if (!videoUrl.includes("youtube.com")) {

            loadingMessage.innerText =
                "Please open a YouTube video first.";

            return;
        }


        // Send request to backend
        const response = await fetch(
            "http://127.0.0.1:8000/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    url: videoUrl,
                    question: question
                })
            }
        );


        // Check HTTP errors
        if (!response.ok) {

            throw new Error(
                `HTTP Error: ${response.status}`
            );
        }


        // Convert response to JSON
        const data = await response.json();

        console.log("Backend Response:", data);


        // Handle backend response safely
        if (data.answer) {

            loadingMessage.innerText =
                data.answer;

        }

        else if (data.error) {

            loadingMessage.innerText =
                data.error;

        }

        else {

            loadingMessage.innerText =
                "No valid response received.";
        }

    }

    catch (error) {

        console.error("Frontend Error:", error);

        loadingMessage.innerText =
            "Something went wrong.";
    }

});



questionInput.addEventListener("keydown", (event) => {

    if (
        event.key === "Enter" &&
        !event.shiftKey
    ) {

        event.preventDefault();

        askBtn.click();
    }
});