import { useState } from "react";

import {
  GitCompare,
  Loader2,
} from "lucide-react";

import {
  getPlayerComparison,
} from "../../services/api";

export default function Comparisons() {

  const [player1, setPlayer1] = useState("");

  const [player2, setPlayer2] = useState("");

  const [comparison, setComparison] = useState([]);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  async function comparePlayers() {

    if (!player1 || !player2) return;

    setLoading(true);

    setError("");

    try {

      const response = await getPlayerComparison(

        player1,

        player2

      );

      setComparison(response);

    }

    catch (err) {

      console.error(err);

      setError(

        err.response?.data?.detail ||

        "Unable to compare players."

      );

      setComparison([]);

    }

    finally {

      setLoading(false);

    }

  }

  return (

    <div className="max-w-7xl mx-auto py-10 px-6">

      <div className="mb-10">

        <h1 className="text-4xl font-bold">

          ⚖️ Player Comparison

        </h1>

        <p className="text-slate-400 mt-3">

          Compare two Premier League players using statistics from the analytics engine.

        </p>

      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8">

        <div className="grid md:grid-cols-2 gap-6">

          <div>

            <label className="block mb-2 text-slate-300">

              Player 1

            </label>

            <input

              value={player1}

              onChange={(e)=>setPlayer1(e.target.value)}

              placeholder="Harry Kane"

              className="w-full bg-slate-950 border border-slate-700 rounded-xl px-5 py-4"

            />

          </div>

          <div>

            <label className="block mb-2 text-slate-300">

              Player 2

            </label>

            <input

              value={player2}

              onChange={(e)=>setPlayer2(e.target.value)}

              placeholder="Mohamed Salah"

              className="w-full bg-slate-950 border border-slate-700 rounded-xl px-5 py-4"

            />

          </div>

        </div>

        <button

          onClick={comparePlayers}

          disabled={loading}

          className="mt-8 bg-blue-600 hover:bg-blue-700 transition px-8 py-4 rounded-xl flex items-center gap-3"

        >

          {loading ? (

            <Loader2

              size={20}

              className="animate-spin"

            />

          ) : (

            <GitCompare size={20}/>

          )}

          Compare Players

        </button>

                {/* Loading */}

        {loading && (

          <div className="mt-10 flex items-center gap-3">

            <Loader2
              size={22}
              className="animate-spin text-blue-500"
            />

            <span className="text-slate-300">

              Comparing players...

            </span>

          </div>

        )}

        {/* Error */}

        {!loading && error && (

          <div className="mt-10 bg-red-600/20 border border-red-500 rounded-xl p-5">

            <h3 className="font-bold text-red-400">

              Comparison Failed

            </h3>

            <p className="mt-2 text-slate-300">

              {error}

            </p>

          </div>

        )}

        {/* Comparison */}

        {!loading && comparison.length > 0 && (

          <div className="mt-10">

            <h2 className="text-2xl font-bold mb-6">

              Comparison Result

            </h2>

            <div className="overflow-x-auto">

              <table className="w-full border border-slate-800 rounded-xl overflow-hidden">

                <thead className="bg-slate-800">

                  <tr>

                    {Object.keys(comparison[0]).map((column) => (

                      <th
                        key={column}
                        className="px-5 py-4 text-left capitalize"
                      >

                        {column.replaceAll("_"," ")}

                      </th>

                    ))}

                  </tr>

                </thead>

                <tbody>

                  {comparison.map((row,index)=>(

                    <tr
                      key={index}
                      className="border-t border-slate-800 hover:bg-slate-800 transition"
                    >

                      {Object.values(row).map((value,i)=>(

                        <td
                          key={i}
                          className="px-5 py-4"
                        >

                          {String(value)}

                        </td>

                      ))}

                    </tr>

                  ))}

                </tbody>

              </table>

            </div>

          </div>

        )}
                {/* Empty State */}

        {!loading && !error && comparison.length === 0 && (

          <div className="mt-10 bg-slate-950 border border-slate-800 rounded-2xl p-12 text-center">

            <GitCompare
              size={60}
              className="mx-auto text-slate-600 mb-6"
            />

            <h2 className="text-2xl font-bold">

              Ready to Compare

            </h2>

            <p className="text-slate-400 mt-3">

              Enter the names of two Premier League players and click
              <span className="font-semibold text-white">
                {" "}Compare Players
              </span>
              to view a detailed statistical comparison.

            </p>

            <div className="mt-8 flex flex-wrap justify-center gap-3">

              <button
                onClick={() => {
                  setPlayer1("Harry Kane");
                  setPlayer2("Mohamed Salah");
                }}
                className="bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-lg"
              >
                Harry Kane vs Mohamed Salah
              </button>

              <button
                onClick={() => {
                  setPlayer1("Erling Haaland");
                  setPlayer2("Harry Kane");
                }}
                className="bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-lg"
              >
                Haaland vs Kane
              </button>

              <button
                onClick={() => {
                  setPlayer1("Kevin De Bruyne");
                  setPlayer2("Bruno Fernandes");
                }}
                className="bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-lg"
              >
                De Bruyne vs Bruno
              </button>

            </div>

          </div>

        )}

      </div>

      <div className="mt-8 text-center text-slate-500 text-sm">

        PremierIQ Analytics • Compare Premier League players using historical statistics

      </div>

    </div>

  );

}