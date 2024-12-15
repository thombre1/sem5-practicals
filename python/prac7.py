from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

# Create the Bayesian Network structure
model = BayesianNetwork([('Rain', 'Traffic'), ('Accident', 'Traffic')])

# Define CPDs
cpd_rain = TabularCPD('Rain', 2, [[0.7], [0.3]])
cpd_accident = TabularCPD('Accident', 2, [[0.8], [0.2]])
cpd_traffic = TabularCPD(
    'Traffic', 2,
    [[0.9, 0.6, 0.7, 0.1],
     [0.1, 0.4, 0.3, 0.9]],
    evidence=['Rain', 'Accident'], evidence_card=[2, 2]
)

# Add CPDs to the model
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic)
model.check_model()

# Query the model
inference = VariableElimination(model)
query_result = inference.query(variables=['Traffic'], evidence={'Rain': 1, 'Accident': 0})
print(query_result)
