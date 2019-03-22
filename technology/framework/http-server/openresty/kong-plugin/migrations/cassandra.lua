return {
  {
    name = "2019-03-18-0001_init_myplugin",
    up = [[
      CREATE TABLE IF NOT EXISTS myplugin(
        id uuid,
        consumer_id uuid,
        key text,
        created_at timestamp,
        PRIMARY KEY (id)
      );
      CREATE INDEX IF NOT EXISTS ON myplugin(key);
      CREATE INDEX IF NOT EXISTS myplugin_consumer_id ON myplugin(consumer_id);
    ]],
    down = [[
      DROP TABLE myplugin;
    ]]
  }
}