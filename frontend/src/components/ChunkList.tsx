import React, { useEffect, useState } from "react";

const ChunkList = () => {
  const [chunks, setChunks] = useState([]);

  useEffect(() => {
    fetch("/data/output.json")
      .then(res => res.json())
      .then(data => setChunks(data));
  }, []);

  return (
    <div>
      <h2>Processed Chunks</h2>
      {chunks.map((chunk, index) => (
        <div key={index} className="chunk-card">
          <p>{chunk.text}</p>
        </div>
      ))}
    </div>
  );
};

export default ChunkList;
