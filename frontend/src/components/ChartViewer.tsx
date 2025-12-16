interface Props {
  data: {
    chart_type: string;
    image_base64: string;
    summary: string;
  };
}

const ChartViewer = ({ data }: Props) => {
  return (
    <div className="card">
      <h3>{data.chart_type.toUpperCase()} Chart</h3>
      <img
        src={`data:image/png;base64,${data.image_base64}`}
        alt="Chart"
        style={{ maxWidth: "100%" }}
      />
      <p>{data.summary}</p>
    </div>
  );
};

export default ChartViewer;
