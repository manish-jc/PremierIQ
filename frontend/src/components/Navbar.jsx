import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-slate-900 border-b border-slate-800">

      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <Link
          to="/"
          className="text-2xl font-bold text-blue-400"
        >
          ⚽ PremierIQ
        </Link>

        <div className="flex gap-6">

          <Link to="/">Home</Link>

          <Link to="/chat">AI Chat</Link>

          <Link to="/rankings">Rankings</Link>

          <Link to="/compare">Compare</Link>

        </div>

      </div>

    </nav>
  );
}