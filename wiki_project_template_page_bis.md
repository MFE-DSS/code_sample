<img src="/path/to/your/logo.png" width="70" style="float: left; margin-right: 30px" />

# [PROJECT_NAME]

**Project Description**

The objective of this project is to prepare data for deployment, useful for visualizing [DATA_ELEMENTS] at various organizational levels. The project is divided into two parts: loading the repository and completing the repository with entity codes from the fact tables. Project execution is automated through a scenario.

**Instructions for Recovery**

First Step:
  Run again the scenario [SCENARIO_NAME]
  
**Checklist for Automation**

| Type | Info |
|------|------|
| Variable connection schema for Loading | __Need To Be Done__ |
| Variable connection schema for Writing | _Not Done_ |
| Check Executive Engine | __Done__ |

**Project General Information**

| Type | Info |
|------|------|
| Refresh frequency | Daily |
| Refresh Hour | [HOUR] |
| Data Used | [DATA_SOURCES] |
| Outputs | [OUTPUTS_DETAILS] |
| Output Usage | [USAGE_DETAILS] |
| Outputs intermediate Steps | [INTERMEDIATE_STEPS] |
| Scenario | [SCENARIOS_DETAILS] |
| Macro Variables | [MACRO_VARIABLES_DETAILS] |
| Writing Connections | [WRITING_CONNECTIONS_DETAILS] |
| Reading Delta or Full | [READING_MODE] |
| Writing Delta or Full | [WRITING_MODE] |

**Project Details**

| Type | Inputs | Location Input |
|------|--------|----------------|

| Type | Outputs | Location Output |
|------|---------|-----------------|
| Shared Dataset | [DATASET_NAME] | [PROJECT_NAME] |

**Scenario Details**

| Inputs | Outputs |
|--------|---------|
| Triggers Type | [TYPE] |
| Triggers Info | [INFO] |
| Reporter Type | [REPORTER_TYPE] |
| Dependencies | [DEPENDENCIES] |
| Scenario Steps with Dependencies | [STEPS_DETAILS] |

**Project Dependencies**

| Type | Before | After |
|------|--------|-------|
| Project | [PROJECT_BEFORE] | [PROJECT_AFTER] |

**DSS Support for Object References**

DSS supports references to objects analogous to classic markdown links, such as datasets, insights, models, and projects. Remember, formatting in markdown requires adherence to syntax rules, such as using two line breaks for a new line and avoiding leading spaces unless intending to change the layout.

**Including Formulae**

You can embed LaTeX for formulae, for example:

When $`a \ne 0`$, there are two solutions to $`ax^2 + bx + c = 0`$.

<div class="alert">
 Note: You can select a wiki article to display on your project's home page.
</div>
