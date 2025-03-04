import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from collections import OrderedDict
import json
import os


# import ckanext.biodigiknow.cli as cli
# import ckanext.biodigiknow.helpers as helpers
# import ckanext.biodigiknow.views as views
from ckanext.biodigiknow.logic import (
    validators
#     action, auth, validators
)


class BiodigiknowPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController)

    # List of fields that should be processed as JSON lists
    # Add fields as needed
    JSON_LIST_FIELDS = [
        'task_cluster',
        'task',
        # Add more fields here
    ]

    def _process_json_list_field(self, value, field_name='unknown'):
        """
        Process a field that should be a JSON list of strings
        
        Args:
            value: The value to process (string or list)
            field_name: Name of field for logging purposes
            
        Returns:
            list: Processed list of strings
        """
        print(f"Incoming {field_name}: {value} of type {type(value)}")
        
        try:
            # If it's a JSON string, parse it
            if isinstance(value, str) and value.strip().startswith('['):
                items = json.loads(value)
            # If it's already a list, use it as is
            elif isinstance(value, list):
                items = value
            else:
                items = []

            # Ensure all items are strings and remove empty values
            items = [str(item).strip() for item in items if item]
            
            print(f"Processed {field_name}: {items}")
            return items
            
        except json.JSONDecodeError:
            print(f"Error parsing JSON for {field_name}: {value}")
            return []
        except Exception as e:
            print(f"Unexpected error processing {field_name}: {str(e)}")
            return []

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        print("Registering public directory:", os.path.join(os.path.dirname(__file__), 'public'))
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "biodigiknow")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    def get_validators(self):
        return validators.get_validators()

    # IFacets

    def dataset_facets(self, facets_dict, package_type):
        """Modify the facets_dict and return it
        """
        new_facets = OrderedDict()
        new_facets['type'] = toolkit._('Digitization Resource Type')
        new_facets['task_cluster'] = toolkit._('Task Clusters')
        new_facets['task'] = toolkit._('Tasks')

        # Add the rest of the facets
        for key, value in facets_dict.items():
            new_facets[key] = value

        return new_facets
    
    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict
    
    def organization_facets(self, facets_dict, organization_type, package_type):
        return facets_dict

    def before_dataset_index(self, pkg_dict):
        # Get the task_cluster value

        for field_name in self.JSON_LIST_FIELDS:
            if field_name in pkg_dict:
                pkg_dict[field_name] = self._process_json_list_field(
                    pkg_dict.get(field_name, ''),
                    field_name
                )
        return pkg_dict
   
    # Required methods with default implementations
    
    def before_dataset_search(self, search_params):
        return search_params

    def after_dataset_search(self, search_results, search_params):
        return search_results

    def before_dataset_view(self, pkg_dict):
        return pkg_dict

    def after_dataset_create(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_update(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_delete(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_show(self, context, pkg_dict):
        return pkg_dict

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def read(self, entity):
        pass
    
