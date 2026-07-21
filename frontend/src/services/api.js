import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

// ======================================
// AI Chat
// ======================================

export const sendChatMessage = async (question) => {
  const response = await api.post("/chat/", {
    question,
  });

  return response.data;
};

// ======================================
// Player Profile
// ======================================

export const getPlayerProfile = async (playerName) => {
  const response = await api.get("/players/profile", {
    params: {
      player_name: playerName,
    },
  });

  return response.data;
};

// ======================================
// Club Profile
// ======================================

export const getClubProfile = async (clubName) => {
  const response = await api.get("/clubs/profile", {
    params: {
      club_name: clubName,
    },
  });

  return response.data;
};

// ======================================
// Rankings
// ======================================

export const getTopScorers = async (season = null) => {
  const response = await api.get("/rankings/top-scorers", {
    params: {
      season,
    },
  });

  return response.data;
};

export const getTopAssists = async (season = null) => {
  const response = await api.get("/rankings/top-assists", {
    params: {
      season,
    },
  });

  return response.data;
};

export const getTopGoalkeepers = async (season = null) => {
  const response = await api.get("/rankings/goalkeepers", {
    params: {
      season,
    },
  });

  return response.data;
};

export const getClubRankings = async (season = null) => {
  const response = await api.get("/rankings/clubs", {
    params: {
      season,
    },
  });

  return response.data;
};

// ======================================
// Player Comparison
// ======================================

export const getPlayerComparison = async (player1, player2) => {
  const response = await api.get("/comparisons/player", {
    params: {
      player1,
      player2,
    },
  });

  return response.data;
};

// ======================================
// Club Comparison
// ======================================

export const getClubComparison = async (club1, club2) => {
  const response = await api.get("/comparisons/club", {
    params: {
      club1,
      club2,
    },
  });

  return response.data;
};

// ======================================
// Season Comparison
// ======================================

export const getSeasonComparison = async (
  season1,
  season2
) => {
  const response = await api.get("/comparisons/season", {
    params: {
      season1,
      season2,
    },
  });

  return response.data;
};

// ======================================
// Export
// ======================================

export default {
  sendChatMessage,
  getPlayerProfile,
  getClubProfile,
  getTopScorers,
  getTopAssists,
  getTopGoalkeepers,
  getClubRankings,
  getPlayerComparison,
  getClubComparison,
getSeasonComparison,
};