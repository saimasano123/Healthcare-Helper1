import React, { useState } from "react";

function QueryForm() {
  const [query, setQuery] = useState("");
  const [hasInsurance, setHasInsurance] = useState(true);
  const [recommendations, setRecommendations] = useState([]);

  async function getRecommendations() {
  const response = await fetch("https://healthcare-helper.onrender.com/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, has_insurance: hasInsurance })
    });
    const data = await response.json();
    setRecommendations(data.recommendations || []);
  }

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Enter your question"
      />
      <label>
        <input
          type="checkbox"
          checked={hasInsurance}
          onChange={e => setHasInsurance(e.target.checked)}
        />
        Has Insurance
      </label>
      <button onClick={getRecommendations}>Get Recommendations</button>

      {/* Display recommendations */}
      <div>
        {recommendations.length > 0 ? (
          recommendations.map((rec, idx) => (
            <div key={idx} className="recommendation-card">
              <h3>{rec.procedure_name}</h3>
              <p>Provider: {rec.provider_name}</p>
              <p>Cost: ${rec.patient_pays}</p>
              <p>Location: {rec.location}</p>
              <p>Reason: {rec.recommendation_reason}</p>
            </div>
          ))
        ) : (
          <p>No recommendations yet.</p>
        )}
      </div>
    </div>
  );
}

export default QueryForm;