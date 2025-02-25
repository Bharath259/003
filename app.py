@app.route('/')
def dashboard():
    # Get data from Google Sheets
    data = get_google_sheet_data()
    
    # Convert to pandas DataFrame for easy handling and manipulation
    df = pd.DataFrame(data)
    
    # Group by category and calculate total amounts
    grouped_data = df.groupby('Category').agg({'Amount': 'sum'}).reset_index()
    
    # Prepare data to send to the frontend
    category_data = grouped_data.to_dict(orient='records')
    
    return render_template('dashboard.html', category_data=category_data)
