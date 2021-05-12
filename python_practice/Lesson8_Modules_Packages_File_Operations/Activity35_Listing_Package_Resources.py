def package_enumerator(package):
    """
    List the resources defined in a package or module.
    """
    resources = dir(package)
    for resource in resources:
        print(resource)
import string
package_enumerator(string)