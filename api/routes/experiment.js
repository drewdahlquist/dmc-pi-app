const express = require("express");

// experimentRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /experiment.
const experimentRoutes = express.Router();

// This section will help you get the current experiment.
experimentRoutes.route("/experiment").get(function (req, res) {
    console.log('/experiment endpoint hit.')

    console.log(req.body)

    res.json()
});

// This section will help you start a new experiment.
experimentRoutes.route("/experiment/start").post(function (req, res) {
    console.log('/experiment/start endpoint hit.')

    console.log(req.body)

    res.json()
});

// This section will help you stop the current experiment.
experimentRoutes.route("/experiment/stop").put(function (req, res) {
    console.log('/experiment/stop endpoint hit.')

    console.log(req.body)

    res.json()
});

// This section will help you (single) cycle the current experiment.
experimentRoutes.route("/experiment/cycle").put(function (req, res) {
    console.log('/experiment/cycle endpoint hit.')

    console.log(req.body)

    res.json()
});

module.exports = experimentRoutes;
