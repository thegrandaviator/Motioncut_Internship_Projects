import streamlit as st
import datetime
import time

# Create the tabs for the application
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['🏚️ Home', '➕ Add', '📖 Read', '📝 Update', '🗑️ Delete', '📊 Summary'])

# Initialize the expense list in the session state if it doesn't already exist
if 'expense_list' not in st.session_state:
    st.session_state['expense_list'] = []

# Get the expense list from the session state
expense_list = st.session_state['expense_list']

# Home tab
with tab1:
    st.header("Welcome to the Expense Tracker app!")
    st.caption("Built by: :blue[Shakti Swarup Panda]")

# Add Expenses tab
with tab2:
  st.header("Add Expenses")
  with st.form(key="add_expense_form", clear_on_submit=True):
    # Get the inputs of the expenses from the user
    date = st.date_input("Date of the Expense: ")
    amount = st.text_input("Amount of the Expense: ")
    category = st.text_input("Category of the Expense: ")

    # Validate the input data
    if not date or not amount or not category:
      st.warning("Please fill in all the fields.")
    elif float(amount) <= 0:
      st.warning("Amount must be a positive number.")

    # Add the expense to the list and update the session state
    add_expense_button = st.form_submit_button("Add")
    if add_expense_button:
      expense_list.append({'date': date, 'amount': amount, 'category': category})
      st.session_state['expense_list'] = expense_list
      success = st.success("Expense added successfully")
      time.sleep(4)
      success.empty()

# Read all Expenses tab
with tab3:
    st.header("Read all Expenses")
    if expense_list:
        st.write("*** Expenses List ***")
        expenses_table = st.table(expense_list)
    else:
        st.write("No Expenses added yet.")

# Update Expenses tab
with tab4:
    st.header("Update Expenses")

    # Create a list of expense items for the selectbox
    choices = [f"{expense['date']}, {expense['amount']}, {expense['category']}" for expense in expense_list]
    selected_expense_index = st.selectbox(
        "Select Expense to be Updated",
        choices if choices else ['Cancel Update']
    )

    # If an expense is selected, allow the user to update its details
    if selected_expense_index is not None and selected_expense_index != 'Cancel Update':
        selected_expense, updated_data = expense_list[choices.index(selected_expense_index)], {}
        with st.form(key="update_expense_form", clear_on_submit=True):
            # Get the updated details from the user
            updated_data['date'] = st.date_input("Update date: ", value=selected_expense.get('date'))
            updated_data['amount'] = st.text_input("Update amount: ", value=selected_expense.get('amount'))
            updated_data['category'] = st.text_input("Update category: ", value=selected_expense.get('category'))

            if not updated_data['date'] or not updated_data['amount'] or not updated_data['category']:
                st.warning("Please fill in all the fields.")
            elif float(updated_data['amount']) <= 0:
                st.warning("Amount must be a positive number.")
            else:
                # Update the expense in the list and the session state
                update_expense_button = st.form_submit_button("Update")
                if update_expense_button:
                    expense_list[choices.index(selected_expense_index)] = {**selected_expense, **updated_data}
                    st.session_state['expense_list'] = expense_list
                    success_update = st.success("Expense updated successfully")
                    time.sleep(3)
                    success_update.empty()
                    st.experimental_rerun()

# Delete Expenses tab
with tab5:
    st.header("Delete Expenses")

    # If there are expenses, allow the user to select and delete an expense
    if expense_list:
        st.write("** Select Expense to Delete **")
        
        choices = [f"{expense['date']}, {expense['amount']}, {expense['category']}" for expense in expense_list]

        with st.form(key="delete_expense_form", clear_on_submit=True):
            selected_expense_index = st.selectbox("Select Expense", choices)

            if selected_expense_index is not None:
                delete_expense_button = st.form_submit_button("Delete")
                
                if delete_expense_button:
                    del_index = choices.index(selected_expense_index)
                    del expense_list[del_index]
                    st.session_state['expense_list'] = expense_list
                    message = st.success("Expense deleted successfully")
                    time.sleep(4)
                    message.empty()
                    st.experimental_rerun()
    else:
        st.write("No expenses to delete.")

# Summary of Expenses tab
with tab6:
    st.header("Show Summary of Expenses")

    # If there are expenses, calculate and display summary
    if expense_list:
        # Calculate the total expenses
        total_expenses = sum(float(expense['amount']) for expense in expense_list)
        st.write(f"Total Expenses: Rs.{total_expenses:.2f}")

        # Calculate the monthly average expenses
        monthly_expenses = {}
        for expense in expense_list:
            expense_date = datetime.datetime.strptime(str(expense['date']), '%Y-%m-%d').date()
            month_year = expense_date.strftime('%b %Y')
            if month_year not in monthly_expenses:
                monthly_expenses[month_year] = []
            monthly_expenses[month_year].append(float(expense['amount']))

        monthly_avg_expenses = {month: sum(amounts)/len(amounts) for month, amounts in monthly_expenses.items()}
        st.write("Monthly Average Expenses:")
        for month, avg_expense in monthly_avg_expenses.items():
            st.write(f"{month}: Rs.{avg_expense:.2f}")

        # Find the minimum and maximum expenses
        min_exp = min(float(expense['amount']) for expense in expense_list)
        max_exp = max(float(expense['amount']) for expense in expense_list)
        st.write(f"Minimum Expenses: Rs.{min_exp:.2f}")
        st.write(f"Max Expenses: Rs.{max_exp:.2f}")

    else:
        st.write("No expenses added yet.")