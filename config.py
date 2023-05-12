def can_build(env, platform):
	return platform in ["x11", "windows", "osx", "server"]

def configure(env):
	pass

def get_doc_classes():
	return [
		"Steam",
	]

def get_doc_path():
	return "doc_classes"
