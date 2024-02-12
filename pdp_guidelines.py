import streamlit as st


# Function to generate accordion sections based on the offering type
def generate_accordion(offering_type):
    if offering_type == "Meal Kit":
        sections = {
            "Sample Menu": """
            ##### From <MONTH OR MENU TITLE>
            * **Dish 1 Name** — Dish 1 Description
            * **Dish 2 Name** — Dish 2 Description
            * …
            * **Pantry Items**

            All meals come fully prepared with accompanying Chef's notes & prep instructions — **simply assemble & serve**.
            """,

            "Additional Perks": f"""
            Your {partner_name} membership also includes:
            * 10% off retail
            * ...

            **INTERNAL NOTE**: If no substantive "additional perks", don't include this section, e.g. no need to highlight things like:
            * Chef's notes
            * "First to know about xyz"
            *
            """,

            "How Membership Works": "You can **skip a month, pause or cancel your membership anytime** via your Table22 member portal.",

            "Who You’re Supporting": "... Stuff about the Chef/establishment from the PLP"
        }
    else:
        sections = {
            "Section 1": "Details for Section 1...",
            "Section 2": "Details for Section 2..."
        }
    return sections

# Streamlit app layout
st.title("PDP Guidelines & Best Practices")
with st.container(border=True):
    st.markdown("""### Overview""")
    # with st.expander("Goals:"):
    st.markdown("""
    This tool aims to provide an up-to-date guide for creating high-quality & _standardized_ PDPs quickly.
    It will be updated as we test into further best practices (e.g. what accordion sections to include, what copy to use, what types of photos to highlight, etc.)

    Currently, it povides guidance on:
    * Default copy for **variant choices** (the dropdowns/boxes users have to select)
    * Recommended **accordion sections** to include (will be updated as we test into / out of others)
    * **Image gallery guidelines**

    The recommendations will be tailored to the offering type (e.g. meal kit vs. wine club), though currently only **meal kit** guidelines have been implemented.
    """)
# with st.expander("""Principles:"""):
    st.markdown("""
    #### High-Level Guidelines:
    1. Concise copy, at the decisio point
        - 1 liner in the top "The Offering" Sections
        - 
        
    2. Use the box structure
    3. Accordions — Meal Kit
        ** Sample Menu
        ** Managing your membership
        ** Who You're Supporting
    4. 5+ high quality photos
    5. Make an **appealing** sample menu
    """)


st.markdown("### Enter Basic Info")
partner_name = st.text_input("Partner Name")
# Offering type selection
offering_type = st.selectbox("Offering Type", ["Meal Kit", "OTHER'S NOT IMPLEMENTED YET"])
if offering_type == "Meal Kit":
    chefs_name = st.text_input("Chef's Name")
# offering_type = st.("Select the type of offering", ["Meal Kit"])


# Display variant choices based on offering type
# variant_choices = get_variant_choices(offering_type)
# st.write("## Variant Choices")
with st.container(border=True):
    st.write("##### The Offering")
    uniq_differentiatior = st.text_area(
        "Enter text for the '[UNIQUE DIFFERENTIATOR]' copy below",
        f"[REPLACE W/ LESS GENERIC COPY]\nsignature {partner_name} dishes, new inspirations, and special off-menu chef’s creations.",
        placeholder=f"signature {partner_name} dishes, new inspirations, and special off-menu chef’s creations.")
    st.write(f"""
    Each month Chef {chefs_name} and our culinary team bring you a **rotating multi-course tasting menu featuring** {uniq_differentiatior}.
    """)
    st.radio("", ["For 2 ($X)", "For 4 ($Y)"], horizontal=True)

with st.container(border=True):
    st.write("##### Food Add-Ons")
    food_addons = st.toggle("Offer food add-ons?")
    if food_addons:
        food_addon_type = st.text_input("What kind?")

with st.container(border=True):
    st.write("##### Beverage Add-Ons")
    bev_pairing_type = st.radio(
        "Which type of Bev. Pairing are we offering?",
        ["None", "Wine", "Cocktail", "Assortment"],
        horizontal=True,
        )
    if bev_pairing_type != "None":
        with st.container(border=True):

            bev_copy = {
                "Wine": dict(
                    title='Wine',
                    desc="Tailored to each month's menu.",

                ),
                "Cocktail": dict(
                    title="Cocktail",
                    desc=""
                ),
                "Assortment": dict(
                    title="Beverage",
                    desc="A monthly curation of wine, cocktails, or whatever we’re feeling — selected to pair with the month’s dishes!"
                ),
            }

            st.write(f"##### Optional {bev_copy.get(bev_pairing_type).get('title')} Pairing")
            st.write(bev_copy.get(bev_pairing_type).get('desc'))
            st.radio("bev choices", ["For 2 (+$X)", "For 4"])

with st.container(border=True):
    st.write("##### Fulfillment Type")
    ff_types = st.multiselect(
        "Which fulfillment types are we offering?",
        ["Pickup", "Delivery",  "Extended Delivery", "Shipping"]
        )
    if ff_types == ['Pickup', 'Delivery']:
        st.write("##### Pickup or Delivery?")
        st.radio(
            "", ["Pickup", "Delivery (+15)"],
            captions=["Pickup at {ADDRESS}", "See delivery range in photos"],
            horizontal=True
        )

# Generate and display accordion sections based on offering type
accordion_sections = generate_accordion(offering_type)
st.write("### Accordion Sections")
for title, content in accordion_sections.items():
    with st.expander(title):
        st.write(content)

st.write("### Photo Guidelines for Food Offering")
with st.expander("See guidelines:"):
    st.markdown("""
    1. Include **5+** QUALITY photos of **food**
        - 3:4 aspect ratio (configure the cropping when uploading)
        - Not blurry (check on desktop)
        - Consider using an instagram photo downloader tool, e.g. https://toolzu.com/downloader/instagram/photo/, to get all the photos from an insta account
    2. When choosing photos:
        - Lead w/ more universally appealling dishes — pastas & chicken parms vs. fish
        - Lead w/ a protein or star dish vs. a dessert or salad
        - Avoid dishes that are ill-suited for at-home, e.g. "tweezer" dishes reliant on plating, raw dishes (ceviches & tartares),
        - If you have a sample menu, try to make some of the photos map to that
    3. Include a photo of the Chef/Owner/Team/space towards the end
    4. If delivery is available, include a photo of the delivery map towards the end
    5. ...

    """)
