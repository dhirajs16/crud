const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching data!", error);
      });
  }, []);

  return (
    <>
      <div>App</div>
    </>
  );
};

export default App;
