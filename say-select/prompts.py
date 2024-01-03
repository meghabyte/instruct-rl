RULE_PROMPT_PREFIX = '''You will be given a list of (OBSERVATION, ACTION, REWARD) examples collected from two agents learning to solve a task.
Possible ACTIONS an agent can take are: 1, 2, 3, 4, 5, and quit.\n
Each OBSERVATION describes the ordered sequence of actions that AGENT 1 picks, and each ACTION describes the ACTION that AGENT 2 picks based on the given OBSERVATION.\n
The examples are seperated into HIGH REWARD and LOW REWARD examples.\n'''
RULE_PROMPT_SUFFIX = '''Output a language instruction that best summarizes the strategy AGENT 2 should follow to receive HIGH REWARD, not LOW REWARD, based on the examples.\n
Start the instruction with the prefix 'I should'.\n'''

EXAMPLE_PROMPT = '''You will be given a list of (OBSERVATION, ACTION, REWARD) examples collected from two agents learning to solve a task.
Possible ACTIONS an agent can take are: 1, 2, 3, 4, 5, and quit. 
AGENT 2 picks an ACTION based on a given OBSERVATION, which describes the ordered sequence of actions that AGENT 1 picked earlier.
The examples are seperated into HIGH REWARD and LOW REWARD examples.

LOW REWARD EXAMPLES: 

OBSERVATION: ['3'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['5'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['1'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['2'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['4'],ACTION: 4,REWARD: 3.84
OBSERVATION: ['3', '3'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['5', '3'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['1', '3'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['2', '3'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['4', '3'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['3', '5'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['5', '5'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['1', '5'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['2', '5'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['4', '5'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['3', '1'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['5', '1'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['1', '1'],ACTION: 2,REWARD: 3.84
OBSERVATION: ['2', '1'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['4', '1'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['3', '2'],ACTION: 2,REWARD: 3.84
OBSERVATION: ['5', '2'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['1', '2'],ACTION: 2,REWARD: 3.84
OBSERVATION: ['2', '2'],ACTION: 1,REWARD: 3.84
OBSERVATION: ['4', '2'],ACTION: 3,REWARD: 3.84
OBSERVATION: ['3', '4'],ACTION: 4,REWARD: 3.84
OBSERVATION: ['5', '4'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['1', '4'],ACTION: 4,REWARD: 3.84
OBSERVATION: ['2', '4'],ACTION: 5,REWARD: 3.84
OBSERVATION: ['4', '4'],ACTION: quit,REWARD: 3.84

HIGH REWARD EXAMPLES:

OBSERVATION: ['3'],ACTION: 3,REWARD: 5.42
OBSERVATION: ['5'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['1'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['2'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['4'],ACTION: 4,REWARD: 5.42
OBSERVATION: ['3', '3'],ACTION: 3,REWARD: 5.42
OBSERVATION: ['5', '3'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['1', '3'],ACTION: 4,REWARD: 5.42
OBSERVATION: ['2', '3'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['4', '3'],ACTION: 3,REWARD: 5.42
OBSERVATION: ['3', '5'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['5', '5'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['1', '5'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['2', '5'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['4', '5'],ACTION: 3,REWARD: 5.42
OBSERVATION: ['3', '1'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['5', '1'],ACTION: quit,REWARD: 5.42
OBSERVATION: ['1', '1'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['2', '1'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['4', '1'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['3', '2'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['5', '2'],ACTION: 1,REWARD: 5.42
OBSERVATION: ['1', '2'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['2', '2'],ACTION: 2,REWARD: 5.42
OBSERVATION: ['4', '2'],ACTION: quit,REWARD: 5.42
OBSERVATION: ['3', '4'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['5', '4'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['1', '4'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['2', '4'],ACTION: 5,REWARD: 5.42
OBSERVATION: ['4', '4'],ACTION: quit,REWARD: 5.42

Based on the examples above, output a language instruction that best summarizes the strategy AGENT 2 should follow when picking an ACTION using the given OBSERVATION in order to receive HIGH REWARD, instead of LOW REWARD.
Start the instruction with the prefix 'I should'. 
'''