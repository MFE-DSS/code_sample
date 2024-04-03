<img src="/static/your_image_directory/logo.png" width="70" style="float: left; margin-right: 30px" />

# Project [PROJECT_NAME] 

The project designers must fill this wiki project documentation to explain items useful for the supervision of projects in [PLATFORM_NAME].

## User guide to fill this WIKI project documentation

2. You have to replace grey text with your own description specific to your project. To illustrate the expected description items, we will use the example of the [EXAMPLE_PROJECT] below. Let's assume that [EXAMPLE_PROJECT] depends on [RELATED_PROJECT]. You have to fill it with your own description.

 <img src="/path/to/your/example_image.png"/>
  
3. Identify your project's final environment based on the given criteria in the column "Which project is eligible for the environmental code?"

We identify a typology of projects with different environmental purposes:

| Target environment code | Target environment label | Which project is eligible for the environmental code? | Benefits | Drawbacks |
|-------------------------|--------------------------|-------------------------------------------------------|----------|-----------|
| E | Exploratory | Projects intended for exploratory mode | Full autonomy for end users | Risk of server overload |
| S | Semi-industrial | Projects intended for industrialized mode | Simplified planning with scenarios | No application supervision |
| P | Production | Projects intended for production mode | Dedicated resources | Restricted access |

## Project Description

Provide a quick description of the purpose of the project, what the assets are, and how often they will be updated.

<u>Example:</u> This project creates a new dataset REF, which is the product ID referential dataset. This output dataset is partitioned by the column "year". The dataset REF is refreshed as soon as the input dataset evolves.

**@users: to be completed**

## Project General Information

| Type | Info |
|------|------|
| Input data connections | [List of data connections] |
| Output data | [Details of outputs: Dataset, Dashboard, etc.] |
| Output data usage | [How the output data is consumed] |
| Variables | [Number of variables] |
| Scenario | [Number of scenarios] |
| Writing connections | [List of writing connections] |
| DELTA or FULL reading mode | [Mode] |
| DELTA or FULL writing mode | [Mode] |

## Inputs Data Details

Provide details on input data, including data connections, Dataiku names, and parent projects.

## Outputs Data Details

Detail the outputs of the project, including the type, connection, and Dataiku name of each output item.

## Scenario Details

Describe each scenario, including the scenario ID, label, triggers, reporters, and dependencies with downstream project scenarios.

## Variable Details

List all variables used in the project, including their functional description and value.

## Project Dependencies

Explain both upstream and downstream project dependencies, if any. Detail the type of dependency (Dataset or Scenario) and provide instructions for identifying scenario dependencies between projects.

### How to know if there is a scenario dependency between my current project and other projects

Provide guidelines for identifying scenario dependencies, both upstream and downstream, including examples and dataset creation progress.

### Upstream Projects Dependencies

| Upstream Projects | Dependency Type |
|-------------------|-----------------|
| [Project Names] | [Type of Dependency] |

### Downstream Projects Dependencies

| Downstream Projects | Dependency Type |
|---------------------|-----------------|
| [Project Names] | [Type of Dependency] |

## Mandatory Information for Industrialization

This section concerns projects that are intended to be semi-industrial or in production.

### Supervision

Explain the supervision process in the production environment, including differences between scenario planning in design and automation nodes.

### Scenario Details

Detail scenarios that are part of the project's industrialization phase, including their IDs, labels, triggers, reporters, and dependencies.

### Instructions for Recovery

Provide instructions for recovering the project's output assets history in case of data issues or other needs, including manual steps to be taken.

**@users: to be completed**
