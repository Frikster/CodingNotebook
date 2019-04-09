# -*- encoding: utf-8 -*-
# stub: pg 1.1.4 ruby lib
# stub: ext/extconf.rb

Gem::Specification.new do |s|
  s.name = "pg"
  s.version = "1.1.4"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib"]
  s.authors = ["Michael Granger", "Lars Kanis"]
  s.cert_chain = ["-----BEGIN CERTIFICATE-----\nMIIENDCCApygAwIBAgIBATANBgkqhkiG9w0BAQsFADAiMSAwHgYDVQQDDBdnZWQv\nREM9RmFlcmllTVVEL0RDPW9yZzAeFw0xODExMjAxODI5NTlaFw0xOTExMjAxODI5\nNTlaMCIxIDAeBgNVBAMMF2dlZC9EQz1GYWVyaWVNVUQvREM9b3JnMIIBojANBgkq\nhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAvyVhkRzvlEs0fe7145BYLfN6njX9ih5H\nL60U0p0euIurpv84op9CNKF9tx+1WKwyQvQP7qFGuZxkSUuWcP/sFhDXL1lWUuIl\nM4uHbGCRmOshDrF4dgnBeOvkHr1fIhPlJm5FO+Vew8tSQmlDsosxLUx+VB7DrVFO\n5PU2AEbf04GGSrmqADGWXeaslaoRdb1fu/0M5qfPTRn5V39sWD9umuDAF9qqil/x\nSl6phTvgBrG8GExHbNZpLARd3xrBYLEFsX7RvBn2UPfgsrtvpdXjsHGfpT3IPN+B\nvQ66lts4alKC69TE5cuKasWBm+16A4aEe3XdZBRNmtOu/g81gvwA7fkJHKllJuaI\ndXzdHqq+zbGZVSQ7pRYHYomD0IiDe1DbIouFnPWmagaBnGHwXkDT2bKKP+s2v21m\nozilJg4aar2okb/RA6VS87o+d7g6LpDDMMQjH4G9OPnJENLdhu8KnPw/ivSVvQw7\nN2I4L/ZOIe2DIVuYH7aLHfjZDQv/mNgpAgMBAAGjdTBzMAkGA1UdEwQCMAAwCwYD\nVR0PBAQDAgSwMB0GA1UdDgQWBBRyjf55EbrHagiRLqt5YAd3yb8k4DAcBgNVHREE\nFTATgRFnZWRARmFlcmllTVVELm9yZzAcBgNVHRIEFTATgRFnZWRARmFlcmllTVVE\nLm9yZzANBgkqhkiG9w0BAQsFAAOCAYEAP9Ffkvg4e8CjIWi8SykQ8oJSS8jbmbgF\nabke3vXWLG6V9kFiObuJd5wZRBluJANu7bEtjgc3fFaGVP2XxVdCpVjNbmMDg4Qp\novvczP53X6pQP2RSZgxF6Lblvy8y11RziUTVRG/Z2aJHsElo6gI7vQznE/OSDrhC\ngEhr8uaIUt7D+HZWRbU0+MkKPpL5uMqaFuJbqXEvSwPTuUuYkDfNfsjQO7ruWBac\nbxHCrvpZ6Tijc0nrlyXi6gPOCLeaqhau2xFnlvKgELwsGYSoKBJyDwqtQ5kwrOlU\ntkSyLrfZ+RZcH535Hyvif7ZxB0v5OxXXoec+N2vrUsEUMRDL9dg4/WFdN8hIOixF\n3IPKpZ1ho0Ya5q7yhygtBK9/NBFHw+nbJjcltfPDBXleRe8u73gnQo8AZIhStYSP\nv4qqqa27Bs468d6SoPxjSm8a2mM9HZ4OdWhq4tFsbTeXDVquCfi64OTEaTt2xQdR\nJnC4lpJfCP6aCXa5h2XAQfPSH636cQap\n-----END CERTIFICATE-----\n"]
  s.date = "2019-01-09"
  s.description = "Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/].\n\nIt works with {PostgreSQL 9.2 and later}[http://www.postgresql.org/support/versioning/].\n\nA small example usage:\n\n  #!/usr/bin/env ruby\n\n  require 'pg'\n\n  # Output a table of current connections to the DB\n  conn = PG.connect( dbname: 'sales' )\n  conn.exec( \"SELECT * FROM pg_stat_activity\" ) do |result|\n    puts \"     PID | User             | Query\"\n    result.each do |row|\n      puts \" %7d | %-16s | %s \" %\n        row.values_at('procpid', 'usename', 'current_query')\n    end\n  end"
  s.email = ["ged@FaerieMUD.org", "lars@greiz-reinsdorf.de"]
  s.extensions = ["ext/extconf.rb"]
  s.extra_rdoc_files = ["Contributors.rdoc", "History.rdoc", "Manifest.txt", "README-OS_X.rdoc", "README-Windows.rdoc", "README.ja.rdoc", "README.rdoc", "ext/errorcodes.txt", "POSTGRES", "LICENSE", "ext/gvl_wrappers.c", "ext/pg.c", "ext/pg_binary_decoder.c", "ext/pg_binary_encoder.c", "ext/pg_coder.c", "ext/pg_connection.c", "ext/pg_copy_coder.c", "ext/pg_errors.c", "ext/pg_result.c", "ext/pg_text_decoder.c", "ext/pg_text_encoder.c", "ext/pg_tuple.c", "ext/pg_type_map.c", "ext/pg_type_map_all_strings.c", "ext/pg_type_map_by_class.c", "ext/pg_type_map_by_column.c", "ext/pg_type_map_by_mri_type.c", "ext/pg_type_map_by_oid.c", "ext/pg_type_map_in_ruby.c", "ext/util.c"]
  s.files = ["Contributors.rdoc", "History.rdoc", "LICENSE", "Manifest.txt", "POSTGRES", "README-OS_X.rdoc", "README-Windows.rdoc", "README.ja.rdoc", "README.rdoc", "ext/errorcodes.txt", "ext/extconf.rb", "ext/gvl_wrappers.c", "ext/pg.c", "ext/pg_binary_decoder.c", "ext/pg_binary_encoder.c", "ext/pg_coder.c", "ext/pg_connection.c", "ext/pg_copy_coder.c", "ext/pg_errors.c", "ext/pg_result.c", "ext/pg_text_decoder.c", "ext/pg_text_encoder.c", "ext/pg_tuple.c", "ext/pg_type_map.c", "ext/pg_type_map_all_strings.c", "ext/pg_type_map_by_class.c", "ext/pg_type_map_by_column.c", "ext/pg_type_map_by_mri_type.c", "ext/pg_type_map_by_oid.c", "ext/pg_type_map_in_ruby.c", "ext/util.c"]
  s.homepage = "https://bitbucket.org/ged/ruby-pg"
  s.licenses = ["BSD-3-Clause"]
  s.rdoc_options = ["--main", "README.rdoc"]
  s.required_ruby_version = Gem::Requirement.new(">= 2.0.0")
  s.rubygems_version = "2.5.1"
  s.summary = "Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/]"

  s.installed_by_version = "2.5.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<hoe-mercurial>, ["~> 1.4"])
      s.add_development_dependency(%q<hoe-deveiate>, ["~> 0.10"])
      s.add_development_dependency(%q<hoe-highline>, ["~> 0.2"])
      s.add_development_dependency(%q<rake-compiler>, ["~> 1.0"])
      s.add_development_dependency(%q<rake-compiler-dock>, ["~> 0.7.0"])
      s.add_development_dependency(%q<hoe-bundler>, ["~> 1.0"])
      s.add_development_dependency(%q<rspec>, ["~> 3.5"])
      s.add_development_dependency(%q<rdoc>, ["~> 5.1"])
      s.add_development_dependency(%q<hoe>, ["~> 3.16"])
    else
      s.add_dependency(%q<hoe-mercurial>, ["~> 1.4"])
      s.add_dependency(%q<hoe-deveiate>, ["~> 0.10"])
      s.add_dependency(%q<hoe-highline>, ["~> 0.2"])
      s.add_dependency(%q<rake-compiler>, ["~> 1.0"])
      s.add_dependency(%q<rake-compiler-dock>, ["~> 0.7.0"])
      s.add_dependency(%q<hoe-bundler>, ["~> 1.0"])
      s.add_dependency(%q<rspec>, ["~> 3.5"])
      s.add_dependency(%q<rdoc>, ["~> 5.1"])
      s.add_dependency(%q<hoe>, ["~> 3.16"])
    end
  else
    s.add_dependency(%q<hoe-mercurial>, ["~> 1.4"])
    s.add_dependency(%q<hoe-deveiate>, ["~> 0.10"])
    s.add_dependency(%q<hoe-highline>, ["~> 0.2"])
    s.add_dependency(%q<rake-compiler>, ["~> 1.0"])
    s.add_dependency(%q<rake-compiler-dock>, ["~> 0.7.0"])
    s.add_dependency(%q<hoe-bundler>, ["~> 1.0"])
    s.add_dependency(%q<rspec>, ["~> 3.5"])
    s.add_dependency(%q<rdoc>, ["~> 5.1"])
    s.add_dependency(%q<hoe>, ["~> 3.16"])
  end
end
