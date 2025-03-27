document.addEventListener("DOMContentLoaded", () => {
    const sendBtn = document.getElementById("send");
    const input = document.getElementById("input");
    const chatBox = document.getElementById("chat-box");

    sendBtn.addEventListener("click", async () => {
        const message = input.value.trim();
        if (!message) return;

        appendMessage("You", message, "user");
        input.value = "";

        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await res.json();
        appendMessage("Bot", data.response, "bot");
    });

    function appendMessage(sender, text, className) {
        const chatBox = document.getElementById("chat-box");
        const div = document.createElement("div");

        const bubbleClass = className === "user" ? "bg-primary text-white" : "bg-secondary text-white";
        div.className = `p-2 my-2 rounded ${bubbleClass} w-75 ${className === "user" ? "ms-auto text-end" : ""}`;
        div.innerHTML = `<strong>${sender}:</strong> ${text}`;

        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

});
