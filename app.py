import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Compound Interest Calculator",
    page_icon=":bar_chart:",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/uckocaman/compound-interest-calculator",
        "Report a Bug": "https://github.com/uckocaman/compound-interest-calculator/issues",
    },
)


def calculate_compound_interest(
    principal,
    annual_rate,
    years,
    monthly_addition,
    annual_addition_increase,
    rate_variance,
):
    def calculate_balance(
        principal, annual_rate, years, monthly_addition, annual_addition_increase
    ):
        balance = principal
        data = {
            "Year": [],
            "Starting Balance": [],
            "Monthly Addition": [],
            "Interest Earned": [],
            "Ending Balance": [],
        }

        for year in range(1, years + 1):
            starting_balance = balance
            # Compound the interest annually on the balance
            interest_earned = balance * (annual_rate / 100)
            balance += interest_earned

            # Add monthly contributions for the year
            for month in range(1, 13):
                balance += monthly_addition

            # Ending balance at the end of the year
            ending_balance = balance

            # Append data to the dictionary
            data["Year"].append(year)
            data["Starting Balance"].append(starting_balance)
            data["Monthly Addition"].append(monthly_addition)
            data["Interest Earned"].append(interest_earned)
            data["Ending Balance"].append(ending_balance)

            # After each year, increase the monthly addition
            monthly_addition *= 1 + (annual_addition_increase / 100)

        return data

    # Calculate balances for the three scenarios
    data_low = calculate_balance(
        principal,
        annual_rate - rate_variance,
        years,
        monthly_addition,
        annual_addition_increase,
    )
    data_mid = calculate_balance(
        principal, annual_rate, years, monthly_addition, annual_addition_increase
    )
    data_high = calculate_balance(
        principal,
        annual_rate + rate_variance,
        years,
        monthly_addition,
        annual_addition_increase,
    )

    # Create DataFrames from the data dictionaries
    df_low = pd.DataFrame(data_low)
    df_mid = pd.DataFrame(data_mid)
    df_high = pd.DataFrame(data_high)

    return df_low, df_mid, df_high


def get_language_settings(language, currency_symbol):
    if language == "English":
        return {
            "title": "Compound Interest Calculator with Interest Rate Variance",
            "labels": {
                "principal": "Initial Principal",
                "annual_rate": "Annual Interest Rate (%)",
                "years": "Number of Years",
                "monthly_addition": "Monthly Addition",
                "annual_addition_increase": "Annual Addition Increase Rate (%)",
                "rate_variance": "Interest Rate Variance (%)",
                "final_balance_low": "Low Interest Rate:",
                "final_balance_mid": "Mid Interest Rate:",
                "final_balance_high": "High Interest Rate:",
                "data_low": "### Data for Low Interest Rate",
                "data_mid": "### Data for Mid Interest Rate",
                "data_high": "### Data for High Interest Rate",
                "plot_title": "Ending Balance Over Time with Interest Rate Variance",
                "xaxis_title": "Year",
                "yaxis_title": f"Ending Balance ({currency_symbol})",
                "final_balance_section": "The final balance with",
                "form_error": "Please fill all the input fields to calculate the compound interest.",
            },
            "help_texts": {
                "principal": "Must be greater than 0",
                "annual_rate": "Annual interest rate in percentage between 1-100%",
                "years": "Investment period in years (must be a positive integer)",
                "monthly_addition": "Monthly contribution amount (must be 0 or greater)",
                "annual_addition_increase": "Annual increase rate for the monthly addition (must be 0 or greater)",
                "rate_variance": "Interest rate variance percentage between 0-100%",
            },
            "about": """
                ## Compound Interest Calculator with Interest Rate Variance
                This application helps you calculate the compound interest with varying interest rates over time.
                You can input your initial principal, annual interest rate, investment period, monthly additions, 
                and annual addition increase rate to see how your investment grows over time.
                
                ### Features:
                - Calculate compound interest with low, mid, and high interest rates.
                - Visualize the growth of your investment with interactive plots.
                - View detailed data for each interest rate scenario.

                Please note that, values produced are for illustrative purposes only and do not constitute advice.
            """,
        }
    else:
        return {
            "title": "Faiz Oranı Varyansı ile Bileşik Faiz Hesaplayıcı",
            "labels": {
                "principal": "Başlangıç Ana Parası",
                "annual_rate": "Yıllık Faiz Oranı (%)",
                "years": "Yıl Sayısı",
                "monthly_addition": "Aylık Ek Yatırım",
                "annual_addition_increase": "Yıllık Ek Yatırım Artış Oranı (%)",
                "rate_variance": "Faiz Oranı Varyansı (%)",
                "final_balance_low": "Düşük Faiz Oranı:",
                "final_balance_mid": "Orta Faiz Oranı:",
                "final_balance_high": "Yüksek Faiz Oranı:",
                "data_low": "### Düşük Faiz Oranı için Veriler",
                "data_mid": "### Orta Faiz Oranı için Veriler",
                "data_high": "### Yüksek Faiz Oranı için Veriler",
                "plot_title": "Faiz Oranı Varyansı ile Zaman İçinde Nihai Bakiye",
                "xaxis_title": "Yıl",
                "yaxis_title": f"Nihai Bakiye ({currency_symbol})",
                "final_balance_section": "Nihai Bakiye ile",
                "form_error": "Bileşik faizi hesaplamak için tüm giriş alanlarını doldurunuz.",
            },
            "help_texts": {
                "principal": "0'dan büyük olmalıdır",
                "annual_rate": "1-100% arasında yıllık faiz oranı",
                "years": "Yatırım süresi (pozitif tam sayı olmalıdır)",
                "monthly_addition": "Aylık ek yatırım miktarı (0 veya daha büyük olmalıdır)",
                "annual_addition_increase": "Aylık katkı artış oranı (0 veya daha büyük olmalıdır)",
                "rate_variance": "Faiz oranı değişim yüzdesi (0-100% arası)",
            },
            "about": """
                ## Bileşik Faiz/Getiri Hesaplayıcısı (Faiz Oranı Varyasyonu ile)
                Bu uygulama, zaman içindeki değişen faiz oranlarıyla bileşik faizi hesaplamanıza yardımcı olur.
                Başlangıç ana paranızı, yıllık faiz oranınızı, yatırım sürenizi, aylık eklemelerinizi ve yıllık ekleme artış oranınızı girerek yatırımınızın zaman içinde nasıl büyüdüğünü görebilirsiniz.
                
                ### Özellikler:

                - Düşük, orta ve yüksek faiz oranlarıyla bileşik faizi hesaplayın.
                - Yatırımınızın büyümesini interaktif grafiklerle görselleştirin.
                - Her faiz oranı senaryosu için ayrıntılı verileri görüntüleyin.

                Lütfen üretilen değerlerin yalnızca örnek amaçlı olduğunu ve tavsiye niteliğinde olmadığını unutmayın.
                """,
        }


# Streamlit UI
col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("Select Language / Dil Seçiniz", ["English", "Türkçe"])

with col2:
    currency = st.selectbox(
        "Select Currency", ["₺ - TRY", "$ - USD", "€ - EUR", "£ - GBP"]
    )

# Currency symbol and code
currency_symbol, currency_code = currency.split(" - ")

# Get language-specific settings
settings = get_language_settings(language, currency_symbol)

with st.sidebar:
    st.image("img/sidebar_logo.png", width=200)
    st.markdown(settings["about"], unsafe_allow_html=True)

# Set UI elements
st.title(settings["title"])
principal_label = settings["labels"]["principal"]
principal_help = settings["help_texts"]["principal"]
annual_rate_label = settings["labels"]["annual_rate"]
annual_rate_help = settings["help_texts"]["annual_rate"]
years_label = settings["labels"]["years"]
years_help = settings["help_texts"]["years"]
monthly_addition_label = settings["labels"]["monthly_addition"]
monthly_addition_help = settings["help_texts"]["monthly_addition"]
annual_addition_increase_label = settings["labels"]["annual_addition_increase"]
annual_addition_increase_help = settings["help_texts"]["annual_addition_increase"]
rate_variance_label = settings["labels"]["rate_variance"]
rate_variance_help = settings["help_texts"]["rate_variance"]
final_balance_low_label = settings["labels"]["final_balance_low"]
final_balance_mid_label = settings["labels"]["final_balance_mid"]
final_balance_high_label = settings["labels"]["final_balance_high"]
data_low_label = settings["labels"]["data_low"]
data_mid_label = settings["labels"]["data_mid"]
data_high_label = settings["labels"]["data_high"]
plot_title = settings["labels"]["plot_title"]
xaxis_title = settings["labels"]["xaxis_title"]
yaxis_title = settings["labels"]["yaxis_title"]
final_balance_section_title = settings["labels"]["final_balance_section"]
form_error_message = settings["labels"]["form_error"]

with st.form(key="input_form"):
    principal = st.number_input(
        principal_label, value=1000, step=1000, min_value=1, help=principal_help
    )
    annual_rate = st.number_input(
        annual_rate_label,
        value=7,
        min_value=1,
        max_value=100,
        step=1,
        help=annual_rate_help,
    )
    years = st.number_input(
        years_label, value=10, min_value=1, step=1, format="%d", help=years_help
    )
    monthly_addition = st.number_input(
        monthly_addition_label,
        value="min",
        min_value=0,
        step=1000,
        help=monthly_addition_help,
    )
    annual_addition_increase = st.number_input(
        annual_addition_increase_label,
        value="min",
        min_value=0,
        step=1,
        help=annual_addition_increase_help,
    )
    rate_variance = st.number_input(
        rate_variance_label,
        value="min",
        min_value=0,
        max_value=100,
        step=1,
        help=rate_variance_help,
    )

    # Calculate button
    calculate_button = st.form_submit_button(
        label="Calculate", icon=":material/calculate:"
    )

    if calculate_button:
        # Input validation
        if not (
            principal is None
            or annual_rate is None
            or years is None
            or monthly_addition is None
            or annual_addition_increase is None
            or rate_variance is None
        ):
            df_low, df_mid, df_high = calculate_compound_interest(
                principal,
                annual_rate,
                years,
                monthly_addition,
                annual_addition_increase,
                rate_variance,
            )
            final_balance_low = df_low["Ending Balance"].iloc[-1]
            final_balance_mid = df_mid["Ending Balance"].iloc[-1]
            final_balance_high = df_high["Ending Balance"].iloc[-1]

            st.subheader(final_balance_section_title)
            col1, col2, col3 = st.columns([1, 1, 1])
            col1.metric(
                label=final_balance_low_label,
                value=f"{currency_symbol}{final_balance_low:,.2f}",
            )
            col2.metric(
                label=final_balance_mid_label,
                value=f"{currency_symbol}{final_balance_mid:,.2f}",
            )
            col3.metric(
                label=final_balance_high_label,
                value=f"{currency_symbol}{final_balance_high:,.2f}",
            )

            # Combine data for plotting
            df_low["Scenario"] = "Low Interest Rate"
            df_mid["Scenario"] = "Mid Interest Rate"
            df_high["Scenario"] = "High Interest Rate"
            df_combined = pd.concat([df_low, df_mid, df_high])

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=df_low["Year"],
                    y=df_low["Ending Balance"],
                    mode="lines+markers",
                    name="Low Interest Rate",
                    text=[
                        f"Year: {year}<br>Ending Balance: {currency_symbol}{balance:,.2f}"
                        for year, balance in zip(
                            df_low["Year"], df_low["Ending Balance"]
                        )
                    ],
                    hoverinfo="text",
                    line=dict(color="red"),
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=df_mid["Year"],
                    y=df_mid["Ending Balance"],
                    mode="lines+markers",
                    name="Mid Interest Rate",
                    text=[
                        f"Year: {year}<br>Ending Balance: {currency_symbol}{balance:,.2f}"
                        for year, balance in zip(
                            df_mid["Year"], df_mid["Ending Balance"]
                        )
                    ],
                    hoverinfo="text",
                    line=dict(color="blue"),
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=df_high["Year"],
                    y=df_high["Ending Balance"],
                    mode="lines+markers",
                    name="High Interest Rate",
                    text=[
                        f"Year: {year}<br>Ending Balance: {currency_symbol}{balance:,.2f}"
                        for year, balance in zip(
                            df_high["Year"], df_high["Ending Balance"]
                        )
                    ],
                    hoverinfo="text",
                    line=dict(color="green"),
                )
            )

            # Plot titles
            fig.update_layout(
                title=plot_title,
                xaxis_title=xaxis_title,
                yaxis_title=yaxis_title,
            )

            st.plotly_chart(fig)

            with st.expander(data_low_label):
                st.dataframe(df_low)

            with st.expander(data_mid_label):
                st.dataframe(df_mid)

            with st.expander(data_high_label):
                st.dataframe(df_high)
        else:
            st.error(form_error_message)
