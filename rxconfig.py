import reflex as rx

config = rx.Config(
    app_name="Venta_dominio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)