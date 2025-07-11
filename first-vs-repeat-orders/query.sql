-- Расчёт количества первых и повторных заказов по дням и их доли
SELECT
    date,
    order_type,
    orders_count,
    ROUND(orders_count / SUM(orders_count) OVER(PARTITION BY date), 2) AS orders_share
FROM (
    SELECT
        time::date as date,
        order_type,
        COUNT(order_id) AS orders_count
    FROM (
        SELECT
            order_id,
            time,
            CASE
                WHEN ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY time) = 1 THEN 'Первый'
                ELSE 'Повторный'
            END AS order_type
        FROM user_actions
        WHERE order_id NOT IN (
            SELECT order_id
            FROM user_actions
            WHERE action = 'cancel_order'
        )
    ) AS orders_with_types
    GROUP BY 1, 2
    ORDER BY 1, 2
) AS daily_orders_by_type;
