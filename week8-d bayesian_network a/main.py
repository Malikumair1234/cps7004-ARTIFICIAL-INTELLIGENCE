

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def main():
    # 1. Create a Bayesian Network model
    model = BayesianNetwork([('Cold Weather', 'Getting Sick'),
                              ('Lack of Sleep', 'Getting Sick')])

    # 2. Define the Conditional Probability Distributions (CPDs)
    # P(Cold Weather)
    cpd_cold_weather = TabularCPD(variable='Cold Weather', variable_card=2,
                                  values=[[0.7], [0.3]])  # P(Cold Weather: No = 0.7, Yes = 0.3)

    # P(Lack of Sleep)
    cpd_lack_of_sleep = TabularCPD(variable='Lack of Sleep', variable_card=2,
                                    values=[[0.6], [0.4]])  # P(Lack of Sleep: No = 0.6, Yes = 0.4)

    # P(Getting Sick | Cold Weather, Lack of Sleep)
    cpd_getting_sick = TabularCPD(variable='Getting Sick', variable_card=2,
                                  values=[[0.9, 0.7, 0.8, 0.5],  # P(Getting Sick: No)
                                          [0.1, 0.3, 0.2, 0.5]], # P(Getting Sick: Yes)
                                  evidence=['Cold Weather', 'Lack of Sleep'],
                                  evidence_card=[2, 2])

    # 3. Add CPDs to the model
    model.add_cpds(cpd_cold_weather, cpd_lack_of_sleep, cpd_getting_sick)

    # 4. Check the model for consistency
    assert model.check_model()

    # 5. Perform inference
    inference = VariableElimination(model)

    # Example of making a query
    print("Query: Probability of Getting Sick given Cold Weather = Yes and Lack of Sleep = Yes")
    result = inference.query(variables=['Getting Sick'], 
                             evidence={'Cold Weather': 1, 'Lack of Sleep': 1})
    print(result)

# Call the main function to set up the network and run inference
if __name__ == "__main__":
    main()

