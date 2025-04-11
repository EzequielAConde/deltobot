import Users from "./components/Users.jsx";
import Weather from "./components/weather.jsx";
import Itinerary from "./components/Itinerary.jsx";
import Floatingbot from "./components/floatingbot.jsx";

const App = () => {
  return (
    <div className="app-container">
      <Users />
      <Weather />
      <Itinerary />
      <Floatingbot />
    </div>
  );
};

export default App;
