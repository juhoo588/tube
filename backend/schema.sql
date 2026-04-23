-- videos 테이블
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(500),
    channel VARCHAR(200),
    velocity FLOAT,
    ctr FLOAT,
    retention FLOAT,
    trend_score FLOAT,
    viral_probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- keyword_signals 테이블
CREATE TABLE keyword_signals (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(200),
    gap_score FLOAT,
    competition FLOAT,
    search_volume INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- competitor_channels 테이블
CREATE TABLE competitor_channels (
    id SERIAL PRIMARY KEY,
    channel VARCHAR(200),
    viral_ratio FLOAT,
    avg_ctr FLOAT,
    avg_retention FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- viral_patterns 테이블
CREATE TABLE viral_patterns (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(300),
    hook_type VARCHAR(100),
    thumbnail_type VARCHAR(100),
    views_multiplier FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
