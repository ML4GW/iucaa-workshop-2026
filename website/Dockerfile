FROM ruby:3.2
WORKDIR /srv/jekyll

# Pin a single, consistent Bundler version
RUN gem install bundler -v 2.4.19

COPY Gemfile Gemfile.lock ./
RUN bundle config set --local path 'vendor/bundle' && bundle install

EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--watch", "--host", "0.0.0.0"]