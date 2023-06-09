def get_sentiment(email_body: str, cat1:str, cat2: str):
    sentiment = f"""
    Given the email below, classify the following context sentiment as '{cat1}' or '{cat2}', just one word.
    Context:
    {email_body}
    
    Sentiment:"""
    return sentiment

def get_sender(email_body:str):
    prompt = f"""
    Given the email below, find who's sending it. Be concise, one line.
    
    Email:
    {email_body}
    Sender:"""
    return prompt

def get_loan(email_body:str):
    prompt = f"""
    Given the email below, find the loan being requested. Return the numerical representation.
    
    Email:
    {email_body}
    Quantity:"""
    return prompt

def get_purpose(email_body: str):
    prompt = f"""
    Given the email below, what's the purpose of the loan request?
    
    Email:
    {email_body}
    Loan purpose:"""
    return prompt

def get_esg (email_body: str):
    prompt = f"""
    {email_body}
    """
    return prompt

def get_recommendation (sentiment, loan_qty, sender, motivation, esg_data):
    esg_review = "negative" if "negative" in esg_data.lower() else "positive"
    loan_action = esg_review == "positive" and sentiment.lower() != "violent"
    if loan_action:
        loan_action = "approve"
    else:
        loan_action = "deny"
    
    prompt = f"""You are the customer service from ResponsibleLending, with email cservice@resplending.com.
    
    Write an email to {sender} to inform that the loan has been {loan_action}. 
    The motivation has been taken into consideration, which was: {motivation}.
    Format it without any HTML tag. Use informal tone and encourage the sender to stay in touch"""
    return prompt