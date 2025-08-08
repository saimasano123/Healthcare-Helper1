import React, { useState } from "react";
import QueryForm from "./components/QueryForm";
import ResponseCard from "./components/ResponseCard";
import "./styles.css";

function App() {
  const [response, setResponse] = useState(null);

  return (
    <div className="container">
      <h1>Healthcare AI Assistant</h1>
      <QueryForm setResponse={setResponse} />
      {response && <ResponseCard data={response} />}
    </div>
  );
}

export default App;
