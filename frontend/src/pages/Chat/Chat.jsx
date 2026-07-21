import { useState, useRef, useEffect } from "react";
import {
  Send,
  Bot,
  User,
  Loader2,
  RefreshCw,
} from "lucide-react";

import { sendChatMessage } from "../../services/api";

export default function Chat() {

  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text:
        "👋 Welcome to PremierIQ! Ask me anything about the Premier League.",
    },
  ]);

  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const bottomRef = useRef(null);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });

  }, [messages]);

  // =====================================
  // Send Message
  // =====================================

  async function handleSend() {

    if (!question.trim()) return;

    const userQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");

    setLoading(true);

    setError("");

    try {

      const response = await sendChatMessage(userQuestion);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text:
            response.answer ??
            "Sorry, I couldn't answer that.",
        },
      ]);

    } catch (err) {

      console.error(err);

      setError(
        err.response?.data?.detail ??
        "Unable to connect to PremierIQ backend."
      );

    } finally {

      setLoading(false);

    }

  }

  // =====================================
  // Retry
  // =====================================

  function handleRetry() {

    const lastUser = [...messages]
      .reverse()
      .find((m) => m.sender === "user");

    if (lastUser) {

      setQuestion(lastUser.text);

    }

  }

  // =====================================
  // ENTER KEY
  // =====================================

  function handleKeyDown(e) {

    if (e.key === "Enter") {

      e.preventDefault();

      handleSend();

    }

  }

  return (

    <div className="max-w-6xl mx-auto py-10 px-6">

      {/* Header */}

      <div className="mb-10">

        <h1 className="text-4xl font-bold">

          🤖 PremierIQ AI Chat

        </h1>

        <p className="text-slate-400 mt-3">

          Ask anything about players,
          clubs,
          rankings,
          awards,
          comparisons,
          seasons and football history.

        </p>

      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">

        {/* Messages */}

        <div className="h-[550px] overflow-y-auto p-6 space-y-6">

                      {messages.map((message, index) => (

            <div
              key={index}
              className={`flex ${
                message.sender === "user"
                  ? "justify-end"
                  : "justify-start"
              }`}
            >

              <div
                className={`flex gap-3 max-w-3xl ${
                  message.sender === "user"
                    ? "flex-row-reverse"
                    : ""
                }`}
              >

                {/* Avatar */}

                <div
                  className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
                    message.sender === "user"
                      ? "bg-blue-600"
                      : "bg-emerald-600"
                  }`}
                >

                  {message.sender === "user" ? (
                    <User size={18} />
                  ) : (
                    <Bot size={18} />
                  )}

                </div>

                {/* Bubble */}

                <div
                  className={`rounded-2xl px-5 py-4 whitespace-pre-wrap leading-7 ${
                    message.sender === "user"
                      ? "bg-blue-600"
                      : "bg-slate-800"
                  }`}
                >

                  {message.text}

                </div>

              </div>

            </div>

          ))}

          {/* Loading */}

          {loading && (

            <div className="flex items-center gap-3">

              <div className="w-10 h-10 rounded-full bg-emerald-600 flex items-center justify-center">

                <Bot size={18} />

              </div>

              <div className="bg-slate-800 rounded-xl px-5 py-4 flex items-center gap-3">

                <Loader2
                  size={18}
                  className="animate-spin"
                />

                Thinking...

              </div>

            </div>

          )}

          {/* Error */}

          {error && (

            <div className="bg-red-600/20 border border-red-500 rounded-xl p-5">

              <h3 className="font-bold">

                Connection Error

              </h3>

              <p className="mt-2 text-slate-300">

                {error}

              </p>

              <button
                onClick={handleRetry}
                className="mt-5 flex items-center gap-2 bg-red-500 hover:bg-red-600 px-4 py-2 rounded-lg"
              >

                <RefreshCw size={16} />

                Retry

              </button>

            </div>

          )}

          <div ref={bottomRef}></div>

        </div>

        {/* Input Area */}


                <div className="border-t border-slate-800 p-5">

          <div className="flex gap-4">

            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask about players, clubs, rankings, seasons..."
              className="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-5 py-4 outline-none focus:border-blue-500"
            />

            <button
              onClick={handleSend}
              disabled={loading || !question.trim()}
              className="bg-blue-600 hover:bg-blue-700 disabled:bg-slate-700 disabled:cursor-not-allowed transition px-6 rounded-xl flex items-center gap-2"
            >

              {loading ? (

                <Loader2
                  size={18}
                  className="animate-spin"
                />

              ) : (

                <>
                  <Send size={18} />
                  Send
                </>

              )}

            </button>

          </div>

          <div className="mt-4 text-sm text-slate-500">

            Example Questions:

            <div className="flex flex-wrap gap-3 mt-3">

              {[
                "Who is Harry Kane?",
                "Tell me about Manchester United",
                "Top scorers in 2022",
                "Compare Salah and Kane",
              ].map((q) => (

                <button
                  key={q}
                  onClick={() => setQuestion(q)}
                  className="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 transition text-sm"
                >
                  {q}
                </button>

              ))}

            </div>

          </div>

        </div>

      </div>

    </div>

  );

}