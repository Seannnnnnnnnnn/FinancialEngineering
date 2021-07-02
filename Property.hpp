// Property pattern for OOP implementations
//

#ifndef Property_hpp
#define Property_hpp

#include <stdio.h>
#include <string>

template <class Name = std::string, class Type = double>
class Property {
    Name name;
    Type value;
    Property<Name, Type>& operator = (const Property<Name, Type>& source);
public:
    Property();
    Property(const Name& name);
    Property(const Name& name, const Type& value);
    Property(const Property<Name, Type>& source);
    virtual ~Property();
    
    // Accessing functions
    virtual Type operator() () const;
    virtual void operator() (const Type& value);
    
    virtual Name nam() const;
    virtual void nam(const Name& new_name);
    
    bool operator == (const Property<Name, Type>& prop2);
};

#endif /* Property_hpp */
