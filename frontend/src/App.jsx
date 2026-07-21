import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home/Home";
import Chat from "./pages/Chat/Chat";
import PlayerProfile from "./pages/PlayerProfile/PlayerProfile";
import ClubProfile from "./pages/ClubProfile/ClubProfile";
import Rankings from "./pages/Rankings/Rankings";
import Comparisons from "./pages/Comparisons/Comparisons";

import Navbar from "./components/Navbar";

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-slate-950 text-white">

        <Navbar />

        <Routes>

          <Route path="/" element={<Home />} />

          <Route path="/chat" element={<Chat />} />

          <Route
            path="/player/:playerName"
            element={<PlayerProfile />}
          />

          <Route
            path="/club/:clubName"
            element={<ClubProfile />}
          />

          <Route
            path="/rankings"
            element={<Rankings />}
          />

          <Route
            path="/compare"
            element={<Comparisons />}
          />

        </Routes>

      </div>
    </BrowserRouter>
  );
}