return {
  {
    name = "2019-03-18-0001_init_myplugin",
    up = [[
      CREATE TABLE IF NOT EXISTS myplugin(
        id uuid,
        key text UNIQUE,
        consumer_id uuid REFERENCES consumers (id) ON DELETE CASCADE,
        created_at timestamp without time zone default (CURRENT_TIMESTAMP(0) at time zone 'utc'),
        PRIMARY KEY (id)
      );
    ]],
    down = [[
      DROP TABLE myplugin;
    ]]
  }
}