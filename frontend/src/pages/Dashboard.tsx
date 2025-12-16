import { useState } from "react";
import FileUpload from "../components/FileUpload";
import QueryBox from "../components/QueryBox";
import ChartViewer from "../components/ChartViewer";

const Dashboard = () => {
  const [uploaded, setUploaded] = useState(false);
  const [chartData, setChartData] = useState<any>(null);

  return (
    <div className="container">
      <h1>📊 Agentic BI Copilot</h1>
      <p style={{ textAlign: "center", color: "#6b7280", marginBottom: "20px" }}>
        Upload Excel • Ask Questions • Get Business Insights
      </p>

      <FileUpload
        onSuccess={() => {
          setUploaded(true);
          setChartData(null);
        }}
      />

      <QueryBox
        disabled={!uploaded}
        onResult={(data) => setChartData(data)}
      />

      {chartData && <ChartViewer data={chartData} />}
    </div>
  );
};

export default Dashboard;
