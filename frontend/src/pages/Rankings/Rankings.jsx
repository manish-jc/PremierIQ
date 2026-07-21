import { useEffect, useState } from "react";

import {
  Trophy,
  Target,
  Shield,
  Loader2,
} from "lucide-react";

import {
  getTopScorers,
  getTopAssists,
  getTopGoalkeepers,
} from "../../services/api";

export default function Rankings() {

  const [season, setSeason] = useState(2022);

  const [category, setCategory] = useState("scorers");

  const [data, setData] = useState([]);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const seasons = [
    2022,
    2021,
    2020,
    2019,
    2018,
    2017,
    2016,
    2015,
    2014,
    2013,
    2012,
    2011,
    2010,
    2009,
    2008,
    2007,
    2006,
    2005,
    2004,
    2003,
    2002,
    2001,
    2000,
    1999,
    1998,
    1997,
    1996,
    1995,
    1994,
    1993
  ];

  useEffect(() => {

    fetchRankings();

  }, [season, category]);

  async function fetchRankings() {

    setLoading(true);

    setError("");

    try {

      let response;

      if (category === "scorers") {

        response = await getTopScorers(season);

      }

      else if (category === "assists") {

        response = await getTopAssists(season);

      }

      else if (category === "goalkeepers") {

        response = await getTopGoalkeepers(season);

      }

      setData(response);

    }

    catch (err) {

      console.error(err);

      setError("Unable to fetch rankings.");

    }

    finally {

      setLoading(false);

    }

  }

  return (

    <div className="max-w-7xl mx-auto py-10 px-6">

      <div className="flex justify-between items-center mb-8">

        <div>

          <h1 className="text-4xl font-bold">

            🏆 Premier League Rankings

          </h1>

          <p className="text-slate-400 mt-2">

            Explore rankings across every season.

          </p>

        </div>

        <select

          value={season}

          onChange={(e)=>setSeason(Number(e.target.value))}

          className="bg-slate-900 border border-slate-700 rounded-lg px-4 py-3"

        >

          {seasons.map((year)=>(

            <option key={year} value={year}>

              {year}

            </option>

          ))}

        </select>

      </div>

      {/* CATEGORY BUTTONS */}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">

        <button

          onClick={()=>setCategory("scorers")}

          className={`p-4 rounded-xl border transition ${
            category==="scorers"
            ? "bg-blue-600 border-blue-600"
            : "bg-slate-900 border-slate-800 hover:bg-slate-800"
          }`}

        >

          <Trophy className="mx-auto mb-2"/>

          Top Scorers

        </button>

        <button

          onClick={()=>setCategory("assists")}

          className={`p-4 rounded-xl border transition ${
            category==="assists"
            ? "bg-emerald-600 border-emerald-600"
            : "bg-slate-900 border-slate-800 hover:bg-slate-800"
          }`}

        >

          <Target className="mx-auto mb-2"/>

          Top Assists

        </button>

        <button

          onClick={()=>setCategory("goalkeepers")}

          className={`p-4 rounded-xl border transition ${
            category==="goalkeepers"
            ? "bg-orange-600 border-orange-600"
            : "bg-slate-900 border-slate-800 hover:bg-slate-800"
          }`}

        >

          <Shield className="mx-auto mb-2"/>

          Goalkeepers

        </button>

      </div>

            {/* Loading */}

      {loading && (

        <div className="bg-slate-900 rounded-2xl p-16 flex flex-col items-center">

          <Loader2
            size={40}
            className="animate-spin text-blue-500"
          />

          <p className="mt-4 text-slate-400">

            Loading Rankings...

          </p>

        </div>

      )}

      {/* Error */}

      {!loading && error && (

        <div className="bg-red-600/20 border border-red-500 rounded-xl p-6">

          <h2 className="text-xl font-bold">

            Unable to load rankings

          </h2>

          <p className="mt-2 text-slate-300">

            {error}

          </p>

        </div>

      )}

      {/* Rankings Table */}

      {!loading && !error && (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">

          <table className="w-full">

            <thead className="bg-slate-800">

              <tr>

                <th className="text-left px-6 py-4">

                  Rank

                </th>

                <th className="text-left px-6 py-4">

                  Name

                </th>

                <th className="text-left px-6 py-4">

                  Club

                </th>

                <th className="text-left px-6 py-4">

                  {category === "scorers" && "Goals"}

                  {category === "assists" && "Assists"}

                  {category === "goalkeepers" && "Score"}

                </th>

              </tr>

            </thead>

            <tbody>

              {data.map((item, index) => (

                <tr
                  key={index}
                  className="border-t border-slate-800 hover:bg-slate-800 transition"
                >

                  <td className="px-6 py-4 font-bold">

                    #{index + 1}

                  </td>

                  <td className="px-6 py-4">

                    {item.player ||
                     item.player_name ||
                     item.goalkeeper ||
                     item.club_name ||
                     item.club
                     }

                  </td>

                  <td className="px-6 py-4">

                    {item.club ||
                     item.club_name ||
                     "-"}

                  </td>

                  <td className="px-6 py-4 font-semibold text-blue-400">

                    {item.goals ??
 item.assists ??
 item.goalkeeper_score ??
 item.score
 }

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

            {/* Empty State */}

      {!loading && !error && data.length === 0 && (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-16 text-center">

          <Trophy
            size={60}
            className="mx-auto text-slate-600 mb-6"
          />

          <h2 className="text-2xl font-bold">

            No Rankings Found

          </h2>

          <p className="text-slate-400 mt-3">

            No ranking data is available for the selected season.

          </p>

        </div>

      )}

      {/* Footer */}

      <div className="mt-8 text-center text-slate-500 text-sm">

        PremierIQ Analytics • Powered by FastAPI, Gemini AI & Hybrid RAG

      </div>

    </div>

  );

}