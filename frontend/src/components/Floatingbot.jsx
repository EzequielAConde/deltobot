import React from "react";
import "../styles/Floatingbot.css";

const floatingbot = () => {
  return (
    <a
      href="https://t.me/DeltoBot_bot"
      target="_blank"
      rel="noopener noreferrer"
      className="bot-floating"
    >
      <img src="./assets/botdelto.png" alt="DeltoBot" className="bot-img" />
    </a>
  );
};

export default floatingbot;