const express = require("express");
const cors = require("cors");

const authRoutes = require("./routes/authRoutes");

const app = express();


app.use(cors());
app.use(express.json());

// health check
app.get("/", (req, res) => {
  res.send("CampusOne HRIS Auth Server Running");
});

// mount routes
app.use("/auth", authRoutes);

module.exports = app;