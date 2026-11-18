-- GTASIX Neon Postgres schema. Already provisioned 2026-11-18 in separate Neon project.
CREATE TABLE IF NOT EXISTS resource_requests (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  topic TEXT NOT NULL,
  platform TEXT,
  details TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS guide_feedback (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  guide_slug TEXT NOT NULL,
  helpful BOOLEAN NOT NULL,
  details TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS guide_catalog (
  slug TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  category TEXT NOT NULL,
  verification_status TEXT NOT NULL DEFAULT 'VERIFY AT LAUNCH',
  published_at TIMESTAMPTZ DEFAULT now(),
  reviewed_at TIMESTAMPTZ,
  source_urls TEXT[] NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_requests_created ON resource_requests(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_feedback_slug ON guide_feedback(guide_slug);
