import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import {
  User,
  Globe,
  Calendar,
  Ruler,
  Footprints,
  Building2,
  Loader2,
} from "lucide-react";

import { getPlayerProfile } from "../../services/api";

export default function PlayerProfile() {

  const { playerName } = useParams();

  const [player, setPlayer] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {

    async function loadPlayer() {

      try {

        const data = await getPlayerProfile(playerName);

        setPlayer(data);

      }

      catch (err) {

        console.error(err);

        setError("Unable to load player profile.");

      }

      finally {

        setLoading(false);

      }

    }

    loadPlayer();

  }, [playerName]);

  if (loading) {

    return (

      <div className="flex justify-center items-center h-screen">

        <Loader2
          size={45}
          className="animate-spin text-blue-500"
        />

      </div>

    );

  }

  if (error) {

    return (

      <div className="text-center py-24">

        <h2 className="text-red-500 text-3xl">

          {error}

        </h2>

      </div>

    );

  }

  const info = player.player_information;

  const summary = player.career_summary;

  const stats = player.statistics;

  const metrics = player.advanced_metrics;

  return (

    <div className="max-w-7xl mx-auto py-10 px-6">

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

        {/* Header */}

        <div className="flex items-center gap-6">

          <div className="w-28 h-28 rounded-full bg-blue-600 flex justify-center items-center">

            <User size={48} />

          </div>

          <div>

            <h1 className="text-5xl font-bold">

              {info.name}

            </h1>

            <p className="text-slate-400 text-xl mt-2">

              {info.position}

            </p>

            <p className="text-blue-400 mt-2">

              {summary.latest_club}

            </p>

          </div>

        </div>

        {/* Player Information */}

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-12">

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Globe className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Nationality

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              {info.nationality}

            </h2>

          </div>

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Calendar className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Date of Birth

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              {info.date_of_birth}

            </h2>

          </div>

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Ruler className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Height

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              {info.height_cm} cm

            </h2>

          </div>

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Footprints className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Preferred Foot

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              {info.preferred_foot}

            </h2>

          </div>

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Building2 className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Seasons Played

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              {summary.seasons_played}

            </h2>

          </div>

          <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

            <Building2 className="text-blue-500 mb-3"/>

            <h3 className="text-slate-400">

              Market Value

            </h3>

            <h2 className="text-2xl font-bold mt-2">

              € {info.market_value_million} M

            </h2>

          </div>

        </div>

                {/* Career Summary */}

        <div className="mt-14">

          <h2 className="text-3xl font-bold mb-6">

            Career Summary

          </h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Latest Club

              </p>

              <h2 className="text-2xl font-bold mt-3">

                {summary.latest_club}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Seasons Played

              </p>

              <h2 className="text-2xl font-bold mt-3">

                {summary.seasons_played}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Best Scoring Season

              </p>

              <h2 className="text-2xl font-bold mt-3">

                {summary.best_scoring_season}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Goals in Best Season

              </p>

              <h2 className="text-2xl font-bold mt-3 text-green-400">

                {summary.best_season_goals}

              </h2>

            </div>

          </div>

        </div>

        {/* Clubs */}

        <div className="mt-12">

          <h2 className="text-3xl font-bold mb-6">

            Clubs Played For

          </h2>

          <div className="flex flex-wrap gap-4">

            {summary.clubs.map((club) => (

              <span
                key={club}
                className="bg-blue-600/20 border border-blue-500 px-5 py-3 rounded-full"
              >

                {club}

              </span>

            ))}

          </div>

        </div>

        {/* Statistics */}

        <div className="mt-14">

          <h2 className="text-3xl font-bold mb-8">

            Career Statistics

          </h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Goals

              </p>

              <h2 className="text-5xl font-bold text-green-400 mt-3">

                {stats.goals}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Assists

              </p>

              <h2 className="text-5xl font-bold text-blue-400 mt-3">

                {stats.assists}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Appearances

              </p>

              <h2 className="text-5xl font-bold text-yellow-400 mt-3">

                {stats.appearances}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Minutes Played

              </p>

              <h2 className="text-5xl font-bold text-purple-400 mt-3">

                {stats.minutes_played}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Shots

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.shots}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Shots On Target

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.shots_on_target}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Passes

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.passes}

              </h2>

            </div>

            <div className="bg-slate-950 rounded-xl border border-slate-800 p-6">

              <p className="text-slate-400">

                Touches

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.touches}

              </h2>

            </div>

          </div>

        </div>

                {/* Advanced Metrics */}

        <div className="mt-14">

          <h2 className="text-3xl font-bold mb-8">

            Advanced Metrics

          </h2>

          <div className="grid md:grid-cols-3 gap-6">

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Goals Per Game

              </p>

              <h2 className="text-5xl font-bold text-green-400 mt-3">

                {metrics.goals_per_game}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Assists Per Game

              </p>

              <h2 className="text-5xl font-bold text-blue-400 mt-3">

                {metrics.assists_per_game}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Minutes Per Goal

              </p>

              <h2 className="text-5xl font-bold text-yellow-400 mt-3">

                {metrics.minutes_per_goal}

              </h2>

            </div>

          </div>

        </div>

        {/* Defensive Statistics */}

        <div className="mt-14">

          <h2 className="text-3xl font-bold mb-8">

            Defensive Statistics

          </h2>

          <div className="grid md:grid-cols-4 gap-6">

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Tackles

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.tackles}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Interceptions

              </p>

              <h2 className="text-4xl font-bold mt-3">

                {stats.interceptions}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Yellow Cards

              </p>

              <h2 className="text-4xl font-bold text-yellow-400 mt-3">

                {stats.yellow_cards}

              </h2>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

              <p className="text-slate-400">

                Red Cards

              </p>

              <h2 className="text-4xl font-bold text-red-500 mt-3">

                {stats.red_cards}

              </h2>

            </div>

          </div>

        </div>

      </div>

    </div>

  );

}