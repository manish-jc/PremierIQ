import { Link, useNavigate } from "react-router-dom";
import {
  Bot,
  Search,
  Trophy,
  Users,
  BarChart3,
  ArrowRight,
  Sparkles,
  Database,
} from "lucide-react";

export default function Home() {
  const navigate = useNavigate();

  const popularQuestions = [
    "Who is Harry Kane?",
    "Compare Mohamed Salah and Erling Haaland",
    "Top scorers in 2022",
    "Tell me about Manchester United",
    "Who won the Premier League in 2023?",
    "Best goalkeeper in 2022",
  ];

  const features = [
    {
      title: "AI Chat",
      icon: Bot,
      description:
        "Ask football questions naturally and receive intelligent answers powered by Hybrid RAG.",
      link: "/chat",
    },
    {
      title: "Player Analytics",
      icon: Users,
      description:
        "Explore player profiles, goals, assists, market value and performance insights.",
      link: "/player/harry-kane",
    },
    {
      title: "Club Analytics",
      icon: BarChart3,
      description:
        "View club history, squad details and season performance analytics.",
      link: "/club/manchester-united",
    },
    {
      title: "Rankings",
      icon: Trophy,
      description:
        "Discover top scorers, assists, goalkeepers and season rankings.",
      link: "/rankings",
    },
    {
      title: "Hybrid RAG",
      icon: Database,
      description:
        "Semantic search combined with Gemini AI for accurate football knowledge retrieval.",
      link: "/chat",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white">

      {/* Hero */}

      <section className="max-w-7xl mx-auto px-6 pt-24 pb-16">

        <div className="text-center">

          <div className="inline-flex items-center gap-2 px-5 py-2 rounded-full border border-blue-500/30 bg-blue-500/10 mb-8">

            <Sparkles className="text-blue-400" size={18} />

            <span className="text-blue-300 text-sm font-medium">

              AI-Powered Premier League Analytics Platform

            </span>

          </div>

          <h1 className="text-7xl font-black tracking-tight">

            Premier
            <span className="text-blue-500">IQ</span>

          </h1>

          <p className="mt-8 text-xl text-slate-300 max-w-4xl mx-auto leading-9">

            Analyze players, clubs and seasons using a modern football analytics
            platform powered by <span className="text-blue-400">Hybrid RAG</span>,
            <span className="text-blue-400"> Gemini AI</span>,
            <span className="text-blue-400"> FastAPI</span> and
            <span className="text-blue-400"> React</span>.

          </p>

          {/* Tech Pills */}

          <div className="flex flex-wrap justify-center gap-3 mt-10">

            {[
              "Hybrid RAG",
              "Gemini AI",
              "FastAPI",
              "React",
              "FAISS",
              "Python",
              "Football Analytics",
            ].map((tag) => (

              <span
                key={tag}
                className="px-4 py-2 rounded-full border border-slate-700 bg-slate-900 text-blue-300 text-sm"
              >
                {tag}
              </span>

            ))}

          </div>

          {/* Buttons */}

          <div className="flex flex-wrap justify-center gap-5 mt-12">

            <button
              onClick={() => navigate("/chat")}
              className="bg-blue-600 hover:bg-blue-700 px-8 py-4 rounded-xl font-semibold flex items-center gap-2 transition"
            >
              🚀 Launch PremierIQ
              <ArrowRight size={18} />
            </button>

            <button
              onClick={() => navigate("/rankings")}
              className="border border-slate-700 hover:border-blue-500 px-8 py-4 rounded-xl font-semibold transition"
            >
              Explore Rankings
            </button>

          </div>

          {/* Search */}

          <div className="mt-16 max-w-3xl mx-auto">

            <div className="flex items-center bg-slate-900 border border-slate-800 rounded-xl px-5 py-4">

              <Search className="text-slate-500" />

              <input
                type="text"
                placeholder='Try: "Who is Harry Kane?"'
                className="bg-transparent flex-1 outline-none px-4"
              />

            </div>

          </div>

        </div>

      </section>

      {/* Statistics */}

      <section className="max-w-7xl mx-auto px-6 py-12">

        <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">

          {[
            { value: "33", label: "Premier League Seasons" },
            { value: "12K+", label: "Players Analysed" },
            { value: "700+", label: "Clubs Covered" },
            { value: "AI", label: "Hybrid RAG Powered" },
          ].map((item) => (

            <div
              key={item.label}
              className="bg-slate-900 border border-slate-800 rounded-2xl p-8 text-center hover:border-blue-500 transition"
            >

              <h2 className="text-4xl font-black text-blue-400">

                {item.value}

              </h2>

              <p className="mt-3 text-slate-400">

                {item.label}

              </p>

            </div>

          ))}

        </div>

      </section>

      {/* Popular Questions */}

      <section className="max-w-6xl mx-auto px-6 py-16">

        <h2 className="text-4xl font-bold mb-10">

          Try asking PremierIQ

        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">

          {popularQuestions.map((question) => (

            <button
              key={question}
              onClick={() =>
                navigate(`/chat?q=${encodeURIComponent(question)}`)
              }
              className="bg-slate-900 border border-slate-800 rounded-xl p-5 text-left hover:border-blue-500 hover:-translate-y-1 transition"
            >

              {question}

            </button>

          ))}

        </div>

      </section>

      {/* Features */}

      <section className="max-w-7xl mx-auto px-6 py-20">

        <div className="text-center mb-14">

          <h2 className="text-5xl font-bold">

            Everything You Need

          </h2>

          <p className="mt-5 text-slate-400 text-lg">

            A complete AI-powered football analytics platform built for
            Premier League exploration.

          </p>

        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

          {features.map((feature) => {

            const Icon = feature.icon;

            return (

              <Link
                key={feature.title}
                to={feature.link}
                className="group bg-slate-900 border border-slate-800 rounded-2xl p-8 hover:border-blue-500 hover:-translate-y-2 transition-all duration-300"
              >

                <div className="w-14 h-14 rounded-xl bg-blue-600/20 flex items-center justify-center mb-6">

                  <Icon size={28} className="text-blue-400" />

                </div>

                <h3 className="text-2xl font-bold mb-4">

                  {feature.title}

                </h3>

                <p className="text-slate-400 leading-7">

                  {feature.description}

                </p>

                <div className="mt-6 flex items-center gap-2 text-blue-400 group-hover:translate-x-2 transition">

                  Explore

                  <ArrowRight size={18} />

                </div>

              </Link>

            );

          })}

        </div>

      </section>

            {/* Why PremierIQ */}

      <section className="bg-slate-900 border-y border-slate-800">

        <div className="max-w-7xl mx-auto px-6 py-24">

          <div className="grid lg:grid-cols-2 gap-16 items-center">

            <div>

              <span className="text-blue-400 uppercase tracking-widest font-semibold">

                Why Choose PremierIQ?

              </span>

              <h2 className="text-5xl font-black mt-4">

                AI Meets Football Analytics

              </h2>

              <p className="mt-8 text-slate-400 text-lg leading-8">

                PremierIQ combines advanced football analytics with
                Retrieval-Augmented Generation (Hybrid RAG) to create a
                conversational analytics platform. Instead of manually
                browsing statistics, simply ask questions in natural
                language and receive intelligent, data-driven answers.

              </p>

              <div className="space-y-8 mt-12">

                <div className="flex gap-5">

                  <div className="w-14 h-14 rounded-xl bg-blue-600/20 flex items-center justify-center text-2xl">

                    ⚽

                  </div>

                  <div>

                    <h3 className="text-xl font-bold">

                      Hybrid RAG Engine

                    </h3>

                    <p className="text-slate-400 mt-2">

                      Combines semantic retrieval with Gemini AI to deliver
                      accurate football insights.

                    </p>

                  </div>

                </div>

                <div className="flex gap-5">

                  <div className="w-14 h-14 rounded-xl bg-blue-600/20 flex items-center justify-center text-2xl">

                    📈

                  </div>

                  <div>

                    <h3 className="text-xl font-bold">

                      Rich Analytics

                    </h3>

                    <p className="text-slate-400 mt-2">

                      Explore player performance, club statistics,
                      rankings, comparisons and season history.

                    </p>

                  </div>

                </div>

                <div className="flex gap-5">

                  <div className="w-14 h-14 rounded-xl bg-blue-600/20 flex items-center justify-center text-2xl">

                    🤖

                  </div>

                  <div>

                    <h3 className="text-xl font-bold">

                      Natural Language Search

                    </h3>

                    <p className="text-slate-400 mt-2">

                      Ask questions just like chatting with a football
                      analyst.

                    </p>

                  </div>

                </div>

              </div>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-3xl p-10">

              <h3 className="text-3xl font-bold mb-8">

                Technology Stack

              </h3>

              <div className="grid grid-cols-2 gap-4">

                {[
                  "Python",
                  "FastAPI",
                  "React",
                  "Tailwind CSS",
                  "Gemini AI",
                  "Hybrid RAG",
                  "FAISS",
                  "Pandas",
                  "REST APIs",
                  "Football Analytics",
                ].map((tech) => (

                  <div
                    key={tech}
                    className="bg-slate-900 rounded-xl border border-slate-800 p-4 text-center font-semibold hover:border-blue-500 transition"
                  >

                    {tech}

                  </div>

                ))}

              </div>

            </div>

          </div>

        </div>

      </section>

      {/* Final CTA */}

      <section className="max-w-7xl mx-auto px-6 py-24">

        <div className="rounded-3xl bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-700 p-16 text-center">

          <h2 className="text-5xl font-black">

            Ready to Explore the Premier League?

          </h2>

          <p className="mt-8 text-blue-100 text-xl max-w-3xl mx-auto leading-8">

            Discover player insights, compare clubs, explore rankings,
            and interact with an AI-powered football assistant built using
            Hybrid RAG.

          </p>

          <div className="flex flex-wrap justify-center gap-5 mt-12">

            <button
              onClick={() => navigate("/chat")}
              className="bg-white text-blue-700 px-8 py-4 rounded-xl font-bold hover:scale-105 transition"
            >
              🚀 Launch AI Chat
            </button>

            <button
              onClick={() => navigate("/compare")}
              className="border border-white px-8 py-4 rounded-xl font-bold hover:bg-white hover:text-blue-700 transition"
            >
              Compare Players
            </button>

          </div>

        </div>

      </section>

      {/* Footer */}

      <footer className="border-t border-slate-800 bg-slate-950">

        <div className="max-w-7xl mx-auto px-6 py-12">

          <div className="flex flex-col lg:flex-row justify-between items-center gap-10">

            <div>

              <h2 className="text-3xl font-black text-blue-500">

                ⚽ PremierIQ

              </h2>

              <p className="text-slate-400 mt-3">

                AI-Powered Premier League Analytics Platform

              </p>

              <p className="text-slate-500 mt-2 text-sm">

                Built using React • FastAPI • Gemini AI • Hybrid RAG • FAISS

              </p>

            </div>

            <div className="flex flex-wrap gap-8 text-slate-400">

              <Link to="/chat" className="hover:text-blue-400 transition">

                AI Chat

              </Link>

              <Link to="/rankings" className="hover:text-blue-400 transition">

                Rankings

              </Link>

              <Link to="/compare" className="hover:text-blue-400 transition">

                Compare

              </Link>

            </div>

          </div>

          <div className="border-t border-slate-800 mt-10 pt-6 text-center text-slate-500 text-sm">

            © 2026 PremierIQ • Built with ❤️ for Football Analytics

          </div>

        </div>

      </footer>

    </div>
  );
}