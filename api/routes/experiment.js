const express = require("express");

// experimentRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /experiment.
const experimentRoutes = express.Router();

// This section will help you get the current experiment.
experimentRoutes.route("/experiment").get(function (req, res) {});

// This section will help you start a new experiment.
experimentRoutes.route("/experiment/start").post(function (req, response) {});

// This section will help you stop the current experiment.
experimentRoutes.route("/experiment/stop").put(function (req, response) {});

// This section will help you (single) cycle the current experiment.
experimentRoutes.route("/experiment/cycle").put(function (req, response) {});

module.exports = experimentRoutes;
