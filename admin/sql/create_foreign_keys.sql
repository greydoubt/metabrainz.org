BEGIN;

ALTER TABLE token
  ADD CONSTRAINT token_owner_id_fkey FOREIGN KEY (owner_id)
  REFERENCES "user" (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE "user"
  ADD CONSTRAINT user_tier_id_fkey FOREIGN KEY (tier_id)
  REFERENCES tier (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE dataset_user
    ADD CONSTRAINT dataset_user_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES "user" (id) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE dataset_user
    ADD CONSTRAINT dataset_user_dataset_id_fkey FOREIGN KEY (dataset_id)
    REFERENCES "dataset" (id) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE token_log
  ADD CONSTRAINT token_log_token_value_fkey FOREIGN KEY (token_value)
  REFERENCES token (value) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE token_log
  ADD CONSTRAINT token_log_user_id_fkey FOREIGN KEY (user_id)
  REFERENCES "user" (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE access_log
  ADD CONSTRAINT access_log_token_fkey FOREIGN KEY (token)
  REFERENCES token (value) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE oauth_client
  ADD CONSTRAINT oauth_client_user_fkey FOREIGN KEY (user_id)
  REFERENCES "user" (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE oauth_grant
  ADD CONSTRAINT oauth_grant_oauth_client_fkey FOREIGN KEY (client_id)
  REFERENCES oauth_client (client_id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE oauth_grant
  ADD CONSTRAINT oauth_grant_user_fkey FOREIGN KEY (user_id)
  REFERENCES "user" (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE oauth_token
  ADD CONSTRAINT oauth_token_oauth_client_fkey FOREIGN KEY (client_id)
  REFERENCES oauth_client (client_id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE oauth_token
  ADD CONSTRAINT oauth_token_user_fkey FOREIGN KEY (user_id)
  REFERENCES "user" (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE;

COMMIT;
