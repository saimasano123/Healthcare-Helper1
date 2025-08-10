import React, { useState } from "react";
import "./css/main.css";

function App() {
  const [response, setResponse] = useState("Waiting for your input...");
  const [recommendations, setRecommendations] = useState([]);
  const [costSummary, setCostSummary] = useState(null);
  const [question, setQuestion] = useState("");
  const [chats, setChats] = useState([]);
  const [activeChat, setActiveChat] = useState(0);

  const [loading, setLoading] = useState(false);
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse("");
    setRecommendations([]);
    setCostSummary(null);
    try {
      const res = await fetch("https://healthcare-helper.onrender.com/api/nlp/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: question }),
      });
      const data = await res.json();
      // Ensure loading indicator is visible for at least 500ms
      setTimeout(() => {
        if (data.response) {
          setResponse("Here are your recommendations:");
          setRecommendations(data.response.recommendations || []);
          setCostSummary(data.response.cost_summary || null);
          // Save chat history
          setChats((prev) => [
            ...prev,
            {
              question,
              response: data.response,
              recommendations: data.response.recommendations || [],
              costSummary: data.response.cost_summary || null,
            },
          ]);
          setActiveChat(chats.length); // Switch to new chat
        } else if (data.error) {
          setResponse(data.error);
        } else {
          setResponse("No recommendations found.");
        }
        setLoading(false);
      }, 500);
    } catch (error) {
      setTimeout(() => {
        setResponse("An error occurred. Please try again.");
        setLoading(false);
      }, 500);
    }
  };

  const showSidebar = recommendations.length > 0 || costSummary !== null;
  return (
    <div className="main-layout">
      {showSidebar && (
        <aside className="sidebar">
          <h2>Chats</h2>
          <button className="new-chat-btn" onClick={() => {
            setQuestion("");
            setResponse("Waiting for your input...");
            setRecommendations([]);
            setCostSummary(null);
            setActiveChat(chats.length);
          }}>+ New Chat</button>
          <ul className="chat-list">
            {chats.map((chat, idx) => (
              <li key={idx} className={activeChat === idx ? "active-chat" : ""} onClick={() => {
                setActiveChat(idx);
                setQuestion(chat.question);
                setResponse("Here are your recommendations:");
                setRecommendations(chat.recommendations);
                setCostSummary(chat.costSummary);
              }}>
                Chat {idx + 1}
              </li>
            ))}
          </ul>
        </aside>
      )}
      <div className="container">
        {(!showSidebar) ? (
          <>
            <h1>Healthcare Helper</h1>
            <form className="form" onSubmit={handleSubmit}>
              <label htmlFor="insurance-upload" className="upload-label">
                Please upload your health insurance document (PDF, JPG, or PNG).
              </label>
              <input
                type="file"
                id="insurance-upload"
                name="insurance"
                accept=".pdf,.jpg,.jpeg,.png"
              />
              <textarea
                rows="6"
                placeholder="Describe your healthcare concern or question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
              ></textarea>
              <button type="submit" disabled={loading} style={{opacity: loading ? 0.6 : 1, cursor: loading ? 'not-allowed' : 'pointer'}}>Submit</button>
            </form>
          </>
        ) : (
          <div className="response-card">
            {loading ? (
              <div className="loading-ellipsis">
                <span></span><span></span><span></span>
              </div>
            ) : (
              <p>{response}</p>
            )}
            {recommendations.length > 0 && (
              <div>
                <h3>Recommendations:</h3>
                <div className="recommendations-list">
                  {recommendations.map((rec, idx) => (
                    <div key={idx} className="recommendation-card">
                      <div className="rec-header">
                        <span className="rec-icon">💡</span>
                        <strong>{rec.procedure_name}</strong>
                      </div>
                      <div className="rec-details">
                        <span className="rec-provider">🏥 {rec.provider_name}</span>
                        <span className="rec-location">📍 {rec.location}</span>
                      </div>
                      <div className="rec-meta">
                        <span className="rec-cost">💲{rec.patient_pays}</span>
                        <span className="rec-quality">⭐ {rec.quality_rating}/5</span>
                        <span className="rec-relevance">🔎 Relevance: {rec.relevance_score}</span>
                      </div>
                      {rec.reason && (
                        <div className="rec-reason">
                          <em>Why this is recommended:</em> {rec.reason}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}
            {costSummary && (
              <div className="cost-summary">
                <h3>Cost Summary:</h3>
                <ul>
                  {Object.entries(costSummary).map(([key, value]) => (
                    <li key={key}>
                      <strong>{key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}:</strong> {value}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;