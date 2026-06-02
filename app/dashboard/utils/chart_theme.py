
# import plotly.graph_objects as go

# def apply_dark_theme(fig):

#     fig.update_layout(

#         template="plotly_dark",

#         paper_bgcolor="rgba(0,0,0,0)",

#         plot_bgcolor="rgba(0,0,0,0)",

#         font=dict(
#             family="Inter",
#             color="#F9FAFB",
#             size=14
#         ),

#         title_font=dict(
#             size=20,
#             color="#F9FAFB"
#         ),

#         margin=dict(
#             l=20,
#             r=20,
#             t=60,
#             b=20
#         ),

#         hoverlabel=dict(
#             bgcolor="#111827",
#             font_size=13,
#             font_family="Inter"
#         ),

#         legend=dict(
#             bgcolor="rgba(0,0,0,0)"
#         )
#     )

#     fig.update_xaxes(
#         showgrid=False,
#         zeroline=False
#     )

#     fig.update_yaxes(
#         gridcolor="rgba(255,255,255,0.08)",
#         zeroline=False
#     )

#     return fig

# =========================================================
# Plotly Enterprise Dark Theme
# =========================================================

def apply_dark_theme(fig):

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.85)",

        font=dict(
            family="Inter",
            color="#F9FAFB",
            size=14
        ),

        title=dict(
            font=dict(
                size=22,
                color="#F9FAFB"
            ),
            x=0.02
        ),

        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.06)",
            zeroline=False
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.06)",
            zeroline=False
        ),

        margin=dict(
            l=40,
            r=40,
            t=60,
            b=40
        ),

        hoverlabel=dict(
            bgcolor="#111827",
            font_size=13
        )
    )

    return fig

