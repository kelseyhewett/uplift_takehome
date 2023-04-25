# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# example Provider:
#  {"id":1,"first_name":"Elisabetta","last_name":"Souten","sex":"Male","birth_date":"1934-12-07","rating":3.6,"primary_skills":["Code Refactoring","Secure Coding Practices","Application Integration"],"secondary_skill":["Web Development"],"company":"Cremin-Vandervort","active":true,"country":"China","language":"Assamese"}
class Provider:
    def __init__(self, id, firstName, lastName, gender, rating, skills, second_skills, company, is_active, country, language):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.rating = rating
        self.skills = skills
        self.second_skills = second_skills
        self.company = company
        self.is_active = is_active
        self.country = country
        self.language = language
        self.freq = 1


class ProviderService:
    def __init__(self, providers):
        # maps Provider.id --> Provider obj
        self.providerList = {}
        for provider in providers:
            self.providerList[provider.id] = provider

    ## CRUD functions for Providers in providerList
    def add_provider(self, provider):
        # Only add the provider if not already in the list
        if provider.id not in self.providerList.keys():
            self.providerList[id] = provider

    def get_provider(self, id):
        if id in self.providerList.keys():
            provider = self.providerList[id]
            provider.freq += 1
            return provider

    def update_provider(self, id, updates={}):
        if id in self.providerList.keys():
            provider = self.providerList[id]
            provider.freq += 1

            # TODO: update to Python 3.10 or switch to if/else
            # for key, value in updates.items():
            #     match key:
            #         case 'firstName':
            #             provider.firstName = value
            #         case 'lastName':
            #             provider.lastName = value
            #         case 'rating':
            #             provider.rating = value
            #         case 'skills':
            #             provider.skills = value
            #         case 'secondSkills':
            #             provider.second_skills = value
            #         case 'company':
            #             provider.company = value
            #         case 'is_active':
            #             provider.is_active = value
            #         case 'country':
            #             provider.country = value
            #         case 'language':
            #             provider.language = value
            #         case 'freq':
            #             provider.freq += 1

    def update_providers(self, providerList):
        for provider in providerList:
            self.update_provider(provider.id, {'freq': 1})

    def remove_provider(self, id):
        if id in self.providerList.keys():
            del(self.providerList[id])

    # Get all active providers
    def get_active_providers(self):
        activeProviders = list(filter(self.is_active, self.providerList.values()))

        # sort by freq, then rating
        sortedProviders = self.sort_providers(activeProviders)

        # update frequency of each provider before returning
        self.update_providers(sortedProviders)
        return sortedProviders

    # given a set of filters, get the provider list
    def get_filtered_providers(self, filters={}):
        providers = self.get_all_providers()

        for key, value in filters.items():
            # filter iteratively
            providers = self.filter_providers(providers, key, value)

        # update frequency of each provider before returning

        # sort by freq, then rating
        sortedProviders = self.sort_providers(providers)
        # update frequency of each provider before returning
        self.update_providers(sortedProviders)
        return sortedProviders

    # return all providers in list
    def get_all_providers(self):
        providers = self.providerList.values()

        self.update_providers(providers)
        providers = self.sort_providers(providers)

        return providers

    ## Helper methods

    # Takes in a pre-filtered list of providers, sorts by frequency then by rating
    def sort_providers(self, filteredList):

        return sorted(filteredList, key=lambda x: (x.rating, x.freq), reverse=True)

    # gets all providers given a single filter key, value pair (e.g. ('rating', 5.0)
    def filter_providers(self, providers, filter_key, filter_value):
        filteredProviders = []

        for provider in providers:
            if filter_key == 'firstName':
                if provider.firstName == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'lastName':
                if provider.lastName == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'gender':
                if provider.gender == filter_value:
                    filteredProviders.append(provider)
            elif filter_key ==  'rating':
                if provider.rating == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'skills':
                if filter_value in provider.skills:
                    filteredProviders.append(provider)
            elif filter_key == 'secondSkills':
                if filter_value in provider.second_skills:
                    filteredProviders.append(provider)
            elif filter_key ==  'company':
                if provider.company == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'is_active':
                if provider.is_active == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'country':
                if provider.country == filter_value:
                    filteredProviders.append(provider)
            elif filter_key == 'language':
                if provider.language == filter_value:
                    filteredProviders.append(provider)

        return filteredProviders

    def is_active(self, provider):
        return provider.is_active

        # # generic filter function based on what attribute we want to filter by
        # # for most, check if value == provider.value (e.g. rating = 5.0)
        # # for lists, check if value in provider.value (e.g. "Scripting" in provider.skills)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p1 = Provider(1, 'Elisabetta', 'Souten', 'Male', 3.6, ["Code Refactoring","Secure Coding Practices","Application Integration"], ["Web Development"], 'Cremin-Vandervort', True, 'China', 'Assamese')
    p2 = Provider(2, 'Alethea', 'Labusch', 'Female', 7.9, ["Computational Logic"], ["Linux / Unix","System Administration","Software Development Lifecycle","Container Technologies"], 'Stanton-Williamson', False, 'China', 'Haitian Creole')
    p3 = Provider(3, 'Hettie', 'Solleme', 'Female', 8.2, ["HTML","Embedded Systems"], ["Continuous Integration"], 'Treutel and Sons', False, 'China', 'Kyrgyz')
    provider_svc = ProviderService([p1, p2, p3])


    # use case 1: get active providers
    active_providers = provider_svc.get_active_providers()
    # Only Elisabetta is active, her freq should be 2
    assert(len(active_providers) == 1)
    for p in active_providers:
        assert(p.is_active == True)
        assert(p.freq == 2)

    # use case 2: get all providers, sorted by freq/rating
    all_providers = provider_svc.get_all_providers()
    # order should be: Elisabetta (highest freq), then Hettie, then Alethea (same freq, Hettie is higher rated)
    assert(len(all_providers) == 3)
    assert(all_providers[0].freq == 2 and all_providers[0].rating == 8.2)
    assert(all_providers[1].freq == 2 and all_providers[1].rating == 7.9)
    assert(all_providers[2].freq == 3 and all_providers[2].rating == 3.6)

    # use case 3: get providers, filtered by any attribute
    filtered_providers = provider_svc.get_filtered_providers({'gender': 'Female'})
    assert(len(filtered_providers) == 2)
    for p in filtered_providers:
        assert(p.gender == 'Female')

    # use case 4: get providers with multiple filtered attributes (including skill list)
    more_filtered_providers = provider_svc.get_filtered_providers({'gender': 'Female', 'skills': 'HTML'})
    assert(len(more_filtered_providers) == 1)
    for p in more_filtered_providers:
        assert(p.gender == 'Female')
        assert('HTML' in p.skills)

