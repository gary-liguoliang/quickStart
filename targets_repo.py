
class TargetsRepo(object):

    repo = {'jira1': 'http://jira1', 'jira2': 'http://jiar2'}

    def get_targets(self, keyword):
        l = list()
        for key, value in TargetsRepo.repo.iteritems():
            if keyword in key:
                l.append(key)

        return l



print TargetsRepo().get_targets("jira")