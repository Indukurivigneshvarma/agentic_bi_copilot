import { useState } from "react";
import { sendQuery } from "../services/api";

interface Props {
  disabled: boolean;
  onResult: (data: any) => void;
}

const QueryBox = ({ disabled, onResult }: Props) => {
  const [query, setQuery] = useState("");

  const handleAsk = async () => {
    if (!query) return;
    const res = await sendQuery(query);
    onResult(res);
  };

  return (
    <div className="card">
      <h3>Ask a Question</h3>
      <input
        type="text"
        placeholder="e.g. Show grade distribution"
        value={query}
        disabled={disabled}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button disabled={disabled} onClick={handleAsk}>
        Ask
      </button>
    </div>
  );
};

export default QueryBox;
