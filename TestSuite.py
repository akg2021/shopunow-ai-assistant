"""
ShopUNow AI Assistant - Test Suite

"""

import os
from datetime import datetime
from shopunow_agent import get_agent


##############################################
# Test 1: Product Information Query (Positive/Neutral)
print("\n TEST 1: Product Information Query\n")
try:
    agent = get_agent()
    print("Agent initialized successfully")
    result = agent.ask(
        "Do you have laptops available? What brands do you carry?"
    )
    print("Result:", result)
    print("Test 1 passed")
except Exception as e:
    print(f"Error in TEST 1: {str(e)}")
    print("Test 1 failed")
    import traceback
    traceback.print_exc()
######################################################

# Test 2: HR Department Query (Positive/Neutral)
print("\n TEST 2: HR Department Query\n")
try:
    agent = get_agent()
    result = agent.ask(
        "What is the maternity leave policy at ShopUNow?"
    )
    print("Result:", result)
    print("Test 2 passed")
except Exception as e:
    print(f"Error in TEST 2: {str(e)}")
    print("Test 2 failed")
    import traceback
    traceback.print_exc()
######################################################
# Test 3: IT Support Query (Neutral)

print("\n TEST 3: IT Support Query\n")
try:
    agent = get_agent()
    result = agent.ask(
        "How do I reset my password?"
    )
    print("Result:", result)
    print("Test 3 passed")
except Exception as e:
    print(f"Error in TEST 3: {str(e)}")
    print("Test 3 failed")
    import traceback
    traceback.print_exc()

######################################################
# Test 4: Multi-Department Query (Neutral)

print("\n TEST 4: Multi-Department Query\n")
try:
    agent = get_agent()
    result = agent.ask(
        "How do I reset my password? What is the maternity leave policy at ShopUNow?    "
    )
    print("Result:", result)
    print("Test 4 passed")
except Exception as e:
    print(f"Error in TEST 4: {str(e)}")
    print("Test 4 failed")
    import traceback
    traceback.print_exc()

######################################################
# Test 5: Negative Sentiment Query (Negative)

print("\n TEST 5: Negative Sentiment Query\n")
try:
    agent = get_agent()
    result = agent.ask(
        "I am very unhappy with the product I received. I want to return it."
    )
    print("Result:", result)
    print("Test 5 passed")
except Exception as e:
    print(f"Error in TEST 5: {str(e)}")
    print("Test 5 failed")
    import traceback
    traceback.print_exc()

######################################################
# Test 6: No Response for any departments (Neutral)

print("\n TEST 6: No Response for any departments\n")
try:
    agent = get_agent()
    result = agent.ask(
        "What is the weather in Tokyo?"
    )
    print("Result:", result)
    print("Test 6 passed")
except Exception as e:
    print(f"Error in TEST 6: {str(e)}")
    print("Test 6 failed")
    import traceback
    traceback.print_exc()
######################################################