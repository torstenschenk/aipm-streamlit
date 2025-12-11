"""
Streamlit Widgets and Session State lab.

Run this file with:
    streamlit run 02_streamlit_widgets_state.py

What to explore:
- Keeping values across reruns with `st.session_state`.
- Using buttons and callbacks to mutate state.
- Grouping inputs with forms.
"""
import streamlit as st

st.set_page_config(page_title="Streamlit Widgets and State", layout="centered")  # Basic page setup

st.title("Counter demo")

if "count" not in st.session_state:
    st.session_state.count = 0  # Initialize state only once per browser session

if "save_count" not in st.session_state:
    st.session_state.save_count = 0  # Track valid form saves across reruns


def increment_save_counter():
    """Callback that bumps the profile save counter when the form is valid."""
    if st.session_state.get("profile_name", "").strip():
        st.session_state.save_count += 1

# vibe coded
count_placeholder = st.empty()  # Reserve space so updates land immediately after button clicks

if st.button("Increment"):
    st.session_state.count += 1  # Button triggers a rerun; state persists

if st.button("Reset"):
    st.session_state.count = 0  # Another button shares the same state store

count_placeholder.write(f"Current count: {st.session_state.count}")

st.caption("State lives across reruns. Combine it with text inputs and selects.")

st.divider()
st.subheader("Profile form")

with st.form("profile"):
    name = st.text_input("Name", key="profile_name")  # Widgets inside a form defer updates
    role = st.selectbox("Role", ["Engineer", "Designer", "PM"])
    subscribed = st.checkbox("Subscribe to updates")
    submitted = st.form_submit_button(
        "Save", on_click=increment_save_counter
    )  # Submission triggers a single rerun

if submitted:
    if not name.strip():  # Simple validation
        st.error("Name is required to save the profile.")
    else:
        st.success(
            f"Saved {name or 'anonymous'} ({role}) | subscribed={subscribed}"
        )  # Form values available after submit
        st.caption(f"Profile saved {st.session_state.save_count} times this session.")

st.markdown(
    """
Stretch goals:
- Add validation (require a name before saving).
- Add a callback that increments a "saves" counter in `st.session_state`.
- Log the state dictionary with `st.write(st.session_state)` to see what Streamlit tracks.
    """
)

st.write(st.session_state)
