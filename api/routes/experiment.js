const express = require("express");

// experimentRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /experiment.
const experimentRoutes = express.Router();

// This section will help you get a list of all the experiments.
experimentRoutes.route("/experiment").get(function (req, res) {});

// This section will help you get a single experiment by id
experimentRoutes.route("/experiment/:id").get(function (req, res) {});

// This section will help you create a new experiment.
experimentRoutes.route("/experiment/add").post(function (req, response) {});

// This section will help you update a experiment by id.
experimentRoutes.route("/update/:id").post(function (req, response) {});

// This section will help you delete a experiment
experimentRoutes.route("/:id").delete((req, response) => {});

module.exports = experimentRoutes;
