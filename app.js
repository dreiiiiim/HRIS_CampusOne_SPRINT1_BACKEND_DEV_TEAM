const express = require("express");
const cors = require("cors");

const authRoutes = require("./src/routes/authRoutes");

const app = express();


app.use(cors({
}));
app.use(express.json());

// health check
app.get("/", (req, res) => {
  res.send("CampusOne HRIS Auth Server Running");
});

// mount routes
app.use("/auth", authRoutes);

//  error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    success: false,
    message: err.message || "Internal Server Error",
  });
});
module.exports = app;